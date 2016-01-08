""" binary search algorithm, O(log n) time complexity """

class BinarySearch:
    def search(self, a, k):
        return self.searchHelper(a, k, 0, len(a) - 1)

    def searchHelper(self, a, k, lo, hi):
        if lo > hi:
            return -1
        mid = lo + (hi - lo) // 2
        if a[k] < a[mid]:
            return self.searchHelper(a, k, lo, mid - 1)
        elif a[k] > a[mid]:
            return self.searchHelper(a, k, mid + 1, hi) 
        else:
            return mid

if __name__ == "__main__":
    a = []
    s = BinarySearch()
    for i in range(100):
        a.append(i)
    print(s.search(a, 13))