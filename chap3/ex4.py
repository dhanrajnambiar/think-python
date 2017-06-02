def do_twice(f,a):
    f(a)
    f(a)
def print_twice(x):
    print(x)
def do_four(g,b):
    do_twice(g,b)
    do_twice(g,b)
do_four(print_twice,'spam')
