def add_all(t):
    total = 0
    for i in t:
        total += i
    return total

def cumulsum_list(s):
    cumulist = []
    i = 0
    while (i < len(s)):
        cumulist.append(add_all(s[0:i + 1]))
        i += 1
    return(cumulist)
x = [2,3,5,6]
print(cumulsum_list(x))
