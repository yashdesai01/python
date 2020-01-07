from zipfile import *
import os

##ZIP file
f=ZipFile("data.zip","w",ZIP_DEFLATED)
f.write("001.jpg")
f.write("002.jpg")
print("Data zip file created")
f.close()

## Un_ZIP file
f=ZipFile("data.zip","r")
current=os.getcwd()
print(current)

f.extractall(current+"\\test1\\")
f.close()
