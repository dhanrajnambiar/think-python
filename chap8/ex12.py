def rot_n(a,n):
    if (a.isupper()):
        if(ord(a) + n > 90):
            temp = (ord(a) + n) - 90
            return(chr(ord('A') + (temp - 1)))
        else:
            return(chr(ord(a) + n))
    if (a.islower()):
        if(ord(a) + n > 122):
            temp = (ord(a) + n) - 122
            return(chr(ord('a') + (temp - 1)))
        else:
            return(chr(ord(a) + n))
a = input('pls enter the word\n')
b = input('enter number of positions to be rotated\n')
for i in a:
    print(rot_n(i,int(b)), end = '')
print('\n')
