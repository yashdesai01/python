file=open("Write","a+")
print("\t Enter data your file")
while(True):
    line=input()
    if(line!="@"):
        file.write(line+"\n")
        continue
    break
file.seek(0,0)
linelist=file.read().splitlines()
print("Reading data from file")
print(linelist)
file.close()
print(linelist)
for eachline in linelist:
    print(eachline)
