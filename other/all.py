##no=int(input("\t Enter the number"))
##loop=1
##temp=no
##while(loop<=no):
##    print(loop,end="\t")
##    loop+=1
##print()

##for loop in range(no):
##    print(loop,end="\t")
##print()

##for loop in range(1,temp+1,2):
##    print(loop,end="\t")
##print()
##abc=["yasbc","ash"]
##abc.sort()
##abc.remove("ash")
##print(abc)

def add(*var):
    print(type(var))
    total=0
    for val in var:
        total+=val
    return total

print(add(1,2,3))
