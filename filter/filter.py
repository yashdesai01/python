def isEven(num):
    if(num%2==0):
        return True
    else:
        return False


def isPos(num):
    if(num>0):
        return True
    else:
        return False

lst=[1,2,4,-22,-66,20]
lstEven=list(filter(isEven,lst))
 
##lstEven=filter(lambda no:(no%2==0),lst)


print("All Num =>",lst)
print(type(lstEven))

for no in lstEven:
    print(no)

#print("Even Number =>",lstEven)
lstPos=list(filter(isPos,lst))
print(lstPos)
