def add(no1,no2):
    return no1+no2

def sub(no1,no2):
    return no1-no2

def mul(no1,no2):
    return no1*no2

def div(no1,no2):
    return no1/no2
while(True):
    print("======CHOISE MENU======")
    print("\t1.ADD")
    print("\t2.SUB")
    print("\t3.MUL")
    print("\t4.DIV")
    print("\t5.exit")
    print("=======================")

    sel=int(input("Enter yout choise=>"))
    if(sel>=5):
        print("bye")
        break
    no1=int(input("Enter the Number No1=>"))
    no2=int(input("Enter the Number no2=>"))

    opr={1:add,2:sub,3:mul,4:div}

    value=int(input("Enter day choise=>"))
    if(value in opr):
        oprvalye = value
        OPR = opr[oprvalue]
        print(oprvalue,"=",OPR)
    else:
        print("Invalid")
        
    ans=opr[sel](no1,no2)
    print(ans)
    continue
