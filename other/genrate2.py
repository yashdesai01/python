##def AllNum(start,end):
##    while start<=end:
##       yield start
##       start+=1
##
##start=int(input("\t strat Value=>"))
##end=int(input("\t end Value=>"))
##ans=AllNum(start,end)
##
##for each in ans:
##    print(each)

def AllNum(start,end):
    while start<=end:
       yield start
       start+=1

def printgen(gen):
    value=next(gen)
    while(True):
        print(value)
        value=next(gen)

start=int(input("\t strat Value=>"))
end=int(input("\t end Value=>"))
ans=AllNum(start,end)

for each in ans:
    print(each)

ans1=printgen(each)
for each1 in ans1:
    print(each1)

 
