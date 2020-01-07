import opr

##print(__name__)
print(type(opr))

a=opr.add(10,20)
print(a)

b=opr.sub(20,10)
print(b)

c=opr.mul(10,20)
print(c)

d=opr.div(20,10)
print(d)

if __name__=="__main__":
    print("call by opr")
else:
    print("call by other file")

