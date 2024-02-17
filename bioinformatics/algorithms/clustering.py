from random import random
from math import inf, exp


def distance(x, y):
    return sum((a - b)**2 for a, b in zip(x, y))**0.5


def dist_to_cluster(point, centres):  # how close is the point to the cluster it is assigned to (i.e. the nearest centre)?
    return min(distance(point, centre) for centre in centres)


def distortion(points, centres):
    return sum(dist_to_cluster(point, centres) ** 2 for point in points) / len(
        points
    )


def farthest_first_clustering(points, k):
    centres = [points[0]]
    points = points[1:]
    for _ in range(k - 1):
        point_dists = [(dist_to_cluster(point, centres), point) for point in points]
        furtherst_away = max(point_dists)
        centres.append(furtherst_away[1])
    return centres


def assign_to_cluster(point, centres):
    best = (inf, 0)
    for centre in range(len(centres)):
        dist = distance(point, centres[centre])
        if dist < best[0]:
            best = (dist, centre)
    return best[1]


def add_vector(a, b):
    if b is None:
        print("STOP")
    return tuple(map(lambda x: x[0]+x[1], zip(a, b)))


def scale_vector(a, q):
    return tuple(map(lambda x: x*q, a))


def centre_of_mass(points):
    n = len(points)
    k = len(points[0])
    o = tuple([0]*k)
    for point in points:
        o = add_vector(o, point)
    return scale_vector(o, 1/n)


def lloyd_kmeans(points, k, initializer=False):
    points = list(points)
    if initializer:
        random.shuffle(points)
    centres = points[:k]
    change = inf
    dist = inf
    while abs(change) > 1e-6:
        assignments = [(point, assign_to_cluster(point, centres)) for point in points]
        clusters = {i: [] for i in range(len(centres))}
        for p, i in assignments:
            clusters[i].append(p)
        centres = [centre_of_mass(clusters[i]) for i in range(len(centres))]
        temp = distortion(points, centres)
        change = dist - temp
        dist = temp
    return centres


def get_responsibilities(point, centres, beta):
    h_vals = [exp(-beta*distance(point, centre)) for centre in centres]
    return [h_val/sum(h_vals) for h_val in h_vals]


def weighted_centre_of_mass(centre: int, responsibilites, k):
    n = len(responsibilites)
    o = tuple([0]*k)
    tot = 0
    for p, r in responsibilites:
        tot += r[centre]
        o = add_vector(o, scale_vector(p, r[centre]))
    return scale_vector(o, 1/tot)


def soft_kmeans(points, k, beta, initializer=False):
    points = list(points)
    if initializer:
        random.shuffle(points)
    centres = points[:k]
    change = inf
    dist = inf
    while abs(change) > 1e-6:
        # E PHASE - Gte hidden
        responsibilities = [(point, get_responsibilities(point, centres, beta)) for point in points]
        # M PHASE - Update centres
        centres = [weighted_centre_of_mass(i, responsibilities, k) for i in range(len(centres))]
        # check convergance speed
        temp = distortion(points, centres)
        change = dist - temp
        dist = temp
    return centres
