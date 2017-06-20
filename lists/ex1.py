def is_dec(a):
    sum_list = 0
    for i in a:
        if type(i) == int:
            sum_list += i
    return(sum_list)
def nested_sum(a):
    summ = 0
    for i in a:
        if (isinstance(i,list)):
            summ += is_dec(i)
        elif (isinstance(i,int)):
            summ += i
    return(summ)
x = [2,3,[2,34,4,'@e'],12]
print(nested_sum(x))
