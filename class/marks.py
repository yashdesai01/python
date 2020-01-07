class student:
    def __init__(s,sub1=0,sub2=0,sub3=0,name=""):
        s.sub1=sub1
        s.sub2=sub2
        s.sub3=sub3
        s.name=name
    def setName(self,name):
        self.name=name
    def SetSub1(self,sub1):
        self.sub1=sub1
    def setSub2(self,sub2):
        self.sub2=sub2
    def setSub3(self,sub3):
        self.sub3=sub3
    def calculateTotal(self):
        self.total=self.sub1+self.sub2+self.sub3
    def calculateper(self):
        self.per=self.total/3
    def passFailsub(self):
        if(self.sub1 > 40 and self.sub2 > 40 and self.sub3>40):
            return True
        else:return False
    def getGrade(self):
        if(self.passFailsub()):
            if(self.per > 80):self.grade = "A+"
            elif(self.per > 70 and self.per<=80):self.grade = "A"
            elif(self.per > 60 and self.per<=70):self.grade = "B+"
            elif(self.per > 50 and self.per<=60):self.grade = "B"
            elif(self.per > 40 and self.per<=50):self.grade = "C"
        else:self.grade="Fail"
    def getAll(self):
        return self.name,self.sub1,self.sub2,self.sub3,self.total,self.per,self.grade
    def getName(self):
        return self.name
def displayAll():
    print("\nSR \tNAME \tMATHS \tHINDI \tENG \tTOTAL \tPER \tGRADE")
    sno=1
    for eachstud in lstStudent:
        print(sno,end="\t")
        each=eachstud.getAll()
        for loop in range(7):
            if(type(each[loop])==float):
                print("%.2f"%(each[loop]),end="\t")
                continue
            print(each[loop],end="\t")
        sno+=1
        print()

def deleteByName(name):
    for loop in range(len(lstStudent)):
        std=lstStudent[loop]
        stdName=std.getName()
        if(stdName.upper() == name.upper()):
            lstStudent.pop(loop)
            return True
        return False
    
lstStudent = []
numstu = int(input("Enter Number of Student=>"))
for loop in range(numstu):
    name=input("Enter name of ["+str(loop+1)+"] Student=>")
    print("student Name=>",name.upper())
    sub1=int(input("Enter mark of maths=>"))
    sub2=int(input("Enter mark of hindi=>"))
    sub3=int(input("Enter mark if English=>"))
    s=student(sub1,sub2,sub3,name)
    s.calculateTotal()
    s.calculateper()
    s.getGrade()
    lstStudent.append(s)
displayAll()

name=input("Enter name for delete=>")
if(deleteByName(name)):
    print(name,"is deleted")
    displayAll()
else:
    print(name,"does not Exists")
            
