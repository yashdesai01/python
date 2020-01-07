line=[]
no=int(input("Enter no of bank account create :-"))
file=open("demo.txt","a+")
for loop in range(no):   
    line=input("Enter Data:-")
##    if line > 0 and line <= 100:
##        print("between 1 to 100")
    file.write(line+"\n")
file.seek(0)
##print("rno\tname\ttotal\tper")
##print()
##for each in file:
##    row=each.split()
##    rno=row[0]
##    name=row[1]
##    total=int(row[2])+int(row[3])+int(row[4])
##    per=total/3
##    print(rno,"\t",name,"\t",total,"\t",per)
##file.close()
