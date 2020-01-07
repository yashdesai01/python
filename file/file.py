## r=read , w=write ,a=append
## r+=write and read ,w+=wrire and read ,a+=append and write
##WAP file write and read in file (a+ use append and write)
##13-09-2019
##file=open("writefile.txt","w")
##line=input("\t Enter the data=>")
##file.write("\n"+line)
##file.close()
##
##file=open("writefile.txt","r")
##line=file.read()
##print(line)
##print(count)

##WAP file wriet and read in file ()
##file=open("writefile.txt","a+")
##line=input("\t Enter the data=>")
##file.write("\n"+line)
##file.seek(0,0)
##line=file.read()
##print(line)
##file.seek(0,0)
##lines=file.read().splitlines()
##print(lines)

#open file search character
##file=open("writefile.txt","a+")
##line=file.read()
##print(line)
##file.seek(0,0)
##search=input("\t Enter the search")
##count=0
##for each in file.read():
##    if each==search:
##        count=count+1
##print(count)
##file.close()

##open file in search word
file=open("yash.txt","r")
line=file.read()
print(line)
file.seek(0,0)
data=file.read()
search=input("\t Enter the search=>")
count=0
for each in data.split():
    if each.upper()==search.upper():
        count=count+1
print(count)
file.close()
