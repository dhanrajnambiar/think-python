def is_triangle(a,b,c):
    if (a > (b + c)):
        print('No')
    elif (b > (a + c)):
        print('No')
    elif (c > (a + b)):
        print('No')
    else:
        print('Yes')
x = input('length of stick1?')
y = input('length of stick2?')
z = input('length of stick3?')
is_triangle(int(x),int(y),int(z))
