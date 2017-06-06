def is_power(a,b):
   if (a % b == 0):
       if ((a / b == 1) or is_power((a / b),b)):
           return True
       else:
           return False
   else:
       return False
a = input('power\n')
b = input('base\n')
x = is_power(int(a),int(b))
print(x)
