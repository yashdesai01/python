getdaynumber = {"mon":1,"tue":2,"wes":3,"thu":4,"fri":5,"sat":6,"sun":7}
getdayname   = {1:"mon",2:"tue",3:"wes",4:"thu",5:"fri",6:"sat",7:"sun"}
while(True):
    print("getdaynumber",getdaynumber)
    print("getdayname",getdayname)

    print("Enter your choise")
    print("1. Getting Day Name")
    print("2. Getting Week Name")

    sel=int(input("Enter your choise=>"))
    if(sel == 1):
        value=int(input("Enter day choise=>"))
        if(value in getdayname):
            daynum = value
            Day = getdayname[daynum]
            print(daynum,"=",Day)
        else:
            print("Invalid")
            
    elif(sel == 2):
        value=input("Enter day Name(only first three character)=>")
        if(len(value)==3 and (value.lower() in getdaynumber)):
            daynumber = getdaynumber[value.lower()]
            print(value,"=",daynumber)
        else:
            print("=Invalid")
    else:
        print("Seletion should be either 1 or 2")

    print(len(getdayname))
    listkey = getdaynumber.keys()
    print("Typs of listkey is",type(listkey),"\n All keys",listkey)

    d1=getdaynumber.copy()
    listvalue = getdaynumber.values()
    print("all value",listvalue)

    for eachkey in getdaynumber:
        print(eachkey,"having",getdaynumber[eachkey],"value")

    print("length",len(listkey))

    for eachkey in listkey:
        print(eachkey,end=" ")

    ##del:getdaynumber["mon"]
    print("After deleting",len(listvalue))
    getdaynumber.clear()
    continue
