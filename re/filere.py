import re
file=open("data.txt","r")
for line in file:
    result=re.findall(r'\S+@\S+',line)
    if len(result) > 0:
        print(result)
file.close()
