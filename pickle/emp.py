import pickle

class emp:
    def __init__(self,emp_id,emp_name,emp_sal,dep_name):
        self.emp_id=emp_id
        self.emp_name=emp_name;
        self.emp_sal=emp_sal;
        self.dep_name=dep_name;

    def getALL(self):
        print(self.emp_id,self.emp_name,self.emp_sal,self.dep_name);

empfile=open("Empbin.dat","wb+")
count=int(input("Enter No of Employee=>"))

for loop in range(count):
    empId=int(input("\tEnter Emp_id=>"))
    empName=input("\tEnter Emp_name=>")
    empSal=int(input("\t Enter salary=>"))
    depName=input("\t Enter department Name=>")
    e=emp(empId,empName,empSal,depName)
    pickle.dump(e,empfile)
empfile.seek(0,0)

while(True):
    try:
        obj=pickle.load(empfile)
##        if(obj.dep_name=="java"):
        obj.getALL()
    except Exception as ex:
        print(ex)
        break
empfile.close()


