def check_fermat(a,b,c,n):
    if (n >= 2):
        lhs = (a ** n + b ** n)
        rhs = (c ** n)
        if (lhs == rhs):
            print('Holy Smokes, Fermat was wrong!')
        else:
            print("No ,that doesn't work")
x = input('Please enter value of a ')
y = input('Please enter value of b ')
z = input('Please enter value of c ')
k = input('Please enter value of exponent ')
check_fermat(int(x),int(y),int(z),int(k))
