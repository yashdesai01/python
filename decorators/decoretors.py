def decoreNot(fun):
    def inner():
        num=int(input("Enter value(for decorenot)"))
        value=fun(num)
        return value+2
    return inner

def getNum(value):
    return value
##@decoreNot
result=decoreNot(getNum)
print(type(result))
value=result()
print(value)

##value1=getNum()
##print(value1)
