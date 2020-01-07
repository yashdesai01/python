from functools import *

lst=[3,4,5]

#with lambda 
result=reduce(lambda x,y,z:pow(x,2)+pow(y,3)+(z-5),lst)

#without lambda 
##def add(x,y):
##    print("x =",x,"y =",y)
##    return pow(x,2)+pow(y,3)+(z-5)

result=reduce(add,lst)
print("Reduce is =",result)
