def square_root(a,b):
    while True:
        print(b)
        y = (b + a / b) / 2
        if (y == b):
            break
        b = y

x = input('number\n')
z = input('approx\n')
square_root(int(x),int(z))

