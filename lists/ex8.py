import random
def has_duplicate(t):
    for i in range(len(t)):
        if (t[i] in t[(i + 1):]):
            return True
        else:
            pass
    return False

def randomgen_list():
    x = []
    for i in range(23):
        x.append(random.randint(0,90))
    return(x)
def prob_calc():
    num_of_dupe = 0
    for i in range(30):#probability is calculated based on thirty experiments
        t = randomgen_list()
        res = has_duplicate(t)
        if (res == True):
            num_of_dupe += 1
    prob = num_of_dupe / 30
    return(prob)
print("The probability of equal aged people = " + str(prob_calc()))
