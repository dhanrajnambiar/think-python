def right_justify(s):
    spaces = ' '
    num = 70 - len(s)
    print(sp * num + s)
string = input()
right_justify(string)
