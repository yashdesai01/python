import os
current=os.getcwd()
name=input("\t\n Enter new directory name=>")
if(os.path.isdir(name)): #isfile -> check whether file exist or not 
    print("directory Already exist")
else:
    os.mkdir(name)
    print("directory created")
    
