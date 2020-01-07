mul=lambda x,y:x*y
maxu=lambda x,y:x if x>y else y
num=lambda allList:[n for n in allList if type(n)==int]

string=lambda allList :[value for value in allList if type(value)==int or type(value)==str]

no1=int(input("\t Enter no1 =>"))
no2=int(input("\t Enter no2 =>"))
ans=mul(no1,no2)

print("Muliplication =>",ans)
print("Maximum=>",maxu(no1,no2))
allList=[1,4,7,"yash",3.4,"jay bhole","har har mahadev"]
mulList=num(allList)
print(mulList)
allstring=string(allList)
print(allstring)
