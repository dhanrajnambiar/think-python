def right_justify(s):
    sp = ' '
    num = 30 - len(s)
    print(sp * num + s)
string = input()
right_justify(string)
