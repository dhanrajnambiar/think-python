def is_rev_strings(x,y):
    if (len(x) != len(y)):
        return False
    i = 0
    j = len(x) -1
    while((i < len(x) - 1) and (j >= 0)):
        if (x[i] == y[j]):
            pass
        else:
            return False
        i += 1
        j -= 1
    return True    
def is_reverse(t):
    temp = []
    for i in range(len(t) - 1):
        for j in t[(i + 1):]:
            if is_rev_strings(t[i],j) == True:
                if t[i] not in temp:
                    temp.append(t[i])
                if j not in temp:
                    temp.append(j)
    return(temp)
test_l = ['banana','ananab','cat','tatoo','tic','tac','ananab']
print(is_reverse(test_l))
