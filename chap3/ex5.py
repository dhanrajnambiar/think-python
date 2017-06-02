def mul_fn(f,val):
    for i in range(val):
        f()
def print_rs():
    print('/',' ' * 4,'/',' ' * 4,'/',' ' * 4,'/',' ' * 4,'/')
def draw_csep():
    mul_fn(print_rs,4)
def print_row():
    print('+','-' * 4,'+','-' * 4,'+','-' * 4,'+','-' * 4,'+')
    draw_csep()
def print_grid():
    mul_fn(print_row,4)
    print('+','-' * 4,'+','-' * 4,'+','-' * 4,'+','-' * 4,'+')
print_grid()
