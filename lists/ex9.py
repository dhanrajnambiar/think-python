def first_duplicate(t):
    for i in range(len(t)):
        if (t[i] in t[(i + 1):]):
            return(t[i])
        else:
            pass
    return False
def remove_duplicates(s):
    while (first_duplicate(s) != False):
        elmnt = first_duplicate(s)
        while (elmnt in s):
            s.remove(elmnt)
