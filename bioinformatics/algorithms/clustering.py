from random import random
from math import inf


def distance(x, y):
    return sum([(a - b)**2 for a, b in zip(x, y)])**0.5


def dist_to_cluster(point, centres):  # how close is the point to the cluster it is assigned to (i.e. the nearest centre)?
    return min([distance(point, centre) for centre in centres])


def distortion(points, centres):
    return sum([dist_to_cluster(point, centres)**2 for point in points])/len(points)


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


def centre_of_mass(points):
    n = len(points)
    k = len(points[0])
    o = tuple([0]*k)
    for point in points:
        o = tuple(map(lambda x: x[0]+x[1], zip(o, point)))
    return tuple(map(lambda x: x/n, o))


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
