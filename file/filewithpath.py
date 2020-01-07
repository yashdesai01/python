import os,sys
print("\t 1. Read from file=>")
print("\t 2. write from file=>")
ch=int(input("\n\tEnter your choise=>"))
filename=input("\n\t Enter file name with extension=>")
if(ch==1):
    if(os.path.isfile(filename)):
        file=open("write","r")
        data=file.read()
        print("\t data from",filename,"\n",data)
    else:
        print("\t file does not exist=>",filename)
elif(ch==2):
    if(os.path.isfile(filename)):
        print(filename,"is already exist,do you want to create(n) or appending data(a)")
        opt=input()
        value=False
        file=''
        if(opt=="n"):
            file=open(filename,"w")
            value=True
        elif(opt=="a"):
            file=open(filename,"a")
            value=True
        else:
            print("\t Invalid opation")

        if(value==True):
            while(True):
                line=input()
                if(line!="@"):
                    file.write(line+"\n")
                    continue
                file.close()
                break
        else:
            file=open(filename,"w")
            while(True):
                line=input()
                if(line!="@"):
                    file.write(line+"\n")
                    continue
                file.close()
                break
    else:
        print("\t Invalid choise")
