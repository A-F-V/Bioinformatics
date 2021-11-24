class BinarySearch:
    def __init__(self, start, end, comparer, emitter=lambda x: x):
        self.start = start
        self.end = end
        self.emitter = emitter  # given the index, returns value to compare
        self.comparer = comparer  # a<goal = neg, a==goal = 0, a>goal = pos

    def search(self, first=True):
        left, right = self.start, self.end
        while right-left > 1:
            mid = (left + right) // 2
            midval = self.emitter(mid)
            comp_val = self.comparer(midval)
            if comp_val < 0:
                left = mid + 1
            elif comp_val > 0:
                right = mid
            else:
                if first:
                    if mid == self.start or self.comparer(self.emitter(mid-1)) != 0:
                        return mid
                    right = mid
                else:
                    if mid == self.end or self.comparer(self.emitter(mid+1)) != 0:
                        return mid
                    left = mid
        return left if self.comparer(self.emitter(left)) == 0 else None
