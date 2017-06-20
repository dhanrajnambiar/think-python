def bisect(t,val):
    low = 0
    high = len(t) - 1
    while (high - low > 1):
        middle = (low + high) // 2
        if (val == t[middle]):
            return middle
        elif (val > t[middle]):
            low = middle
            continue
        elif (val < t[middle]):
            high = middle
            continue
    return None

