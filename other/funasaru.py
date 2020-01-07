def functionasArray(L,F):
    for loop in range(len(L)):
        L[loop]=F(L[loop])

def sumNum(num):
    su=0
    for loop in range(1,num+1):
        su=su+loop
    return su

L=[1,-2,3.33]
print("Before",L)

functionasArray(L,abs)
print("After abc",L)

functionasArray(L,int)
print("after converting in integer",L)

functionasArray(L,factR)
print("after converting in factorial",L)

functionasArray(L,fib)
print("after converting in Fibonnaci",L)

functionasArray(L,sumNum)
print("sum of each Number",L)
