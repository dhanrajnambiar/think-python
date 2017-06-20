def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return(res)
def capitalize_nested(s):
    new = []
    for i in s:
        if (isinstance(i,list)):
            new.append(capitalize_all(i))
        elif (isinstance(i,str)):
            new.append(i.capitalize())
    return(new)
x = ['dhan','cat',['sam','jam','JAG'],'onion']
print(capitalize_nested(x))
