def is_ascending(t):
    l = len(t)
    for i in range(l - 1):
        if (t[i + 1] >= t[i]):
            pass
        else:
            return False
    return True

