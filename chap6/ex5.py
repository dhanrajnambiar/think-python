def ack(m,n):
    if (m < 0):
        return None
    elif (m == 0):
        return(n +1)
    elif (m > 0 and n == 0):
        result = ack(m - 1,1)
        return result
    elif (m > 0 and n > 0):
        temp = ack(m,n - 1)
        return ack(m - 1,temp)
x = ack(3,4)
print(x)
