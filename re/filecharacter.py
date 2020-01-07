import re
file=open("data2.txt","r")
for line in file:
    empcode=re.search(r'\d{4}',line)
    empsalary=re.search(r'\d{4,}.\d{2}',line)
    print("EmpCode:" , empcode.group() , "EmpSalary:" , empsalary.group())
file.close()
    
