##file=open("demo.txt","a+")
##no1=input("\t Enter the Number no1=>")
##no2=input("\t Enter the Number no2=>")
##line=int(no1)+int(no2)
##file.write(no1+"+"+no2+"="+str(line)+"\n ")
##file.seek(0)
##line=file.read()
##print(line)
##file.close()

no=int(input("Enter:-"))
file=open("demo1.txt","a+")
for loop in range(no):
    line=input("Enter Number:-")
    file.write(line+"\n")
file.seek(0)
for each in file:
    row=each.split()
    no1=int(row[0])
    no2=int(row[1])
    add=no1+no2
    print("\n  %d + %d = %d"%(no1,no2,add)+"\n")
    sub=no1-no2
    print("\n  %d - %d = %d"%(no1,no2,sub)+"\n")
    mul=no1 * no2
    print("\n  %d * %d = %d"%(no1,no2,mul)+"\n")
    div=no1//no2
    print("\n  %d / %d = %d"%(no1,no2,div)+"\n")
file.close()

##file=open("demo.txt","a+")
##no1=int(input("\t Enter the Number no1=>"))
##no2=int(input("\t Enter the Number no2=>"))
##ans=no1+no2
##file.write("\n  %d + %d = %d"%(no1,no2,ans)+"\n")
##file.seek(0)
##line=file.read()
##print(line)
##file.close()
        

