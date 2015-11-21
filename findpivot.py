def findpivot(a):
    """ find the index of the pivot element in a, in which the
    elements ascend then descend in values """
    return findPivotHelper(a, 0, len(a) - 1)

def findPivotHelper(a, lo, hi):
    if lo == hi:
        return a[lo]

    mid1 = lo + (hi - lo) // 2
    mid2 = mid1 + 1
    if a[mid1] < a[mid2]:
        return findPivotHelper(a, mid2, hi)
    else:
        return findPivotHelper(a, lo, mid1)

if __name__ == "__main__":
    a = [1,3,4,9,2,0]
    print(findpivot(a))
    
    
