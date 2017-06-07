def eval_loop():
    while True:
        a = input('Plz enter expression to be evaluated\n')
        if (a == 'Done'):
            break
        print(eval(a))
eval_loop()

