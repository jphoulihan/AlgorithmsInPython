# generic binary search function
def binary_search(lo, hi, condition):
    while lo <= hi:

        mid = (lo + hi) // 2
        res = condition(mid)

        if res == 'found':
            return mid
        elif res == 'left':
            hi = mid - 1
        else:
            lo = mid + 1

    return 0