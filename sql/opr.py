import mysql.connector
import insert        
import display
import update
import delete

while(True):
    print("\t== MENU ==")
    print("\t 1.SELECT ")
    print("\t 2.INSERT ")
    print("\t 3.UPDATE ")
    print("\t 4.DELETE ")
    print("\t==========")
    ch=int(input("\t Enter the selection=>"))
    print()
    if(ch>=5):
        print("\t Plz select correct option")
        break
    if(ch==1):
        display.displayALL()
        print()
    elif(ch==2):
        ENAME=input("\t Enter the Ename=>")
        SALARY=int(input("\t Enter the salary=>"))
        DEPID=int(input("\t Enter the depId=>"))
        insert.insertdata(ENAME,SALARY,DEPID)
    elif(ch==3):
        ENAME=input("\t Enter the Ename=>")
        SALARY=int(input("\t Enter the salary=>"))
        DEPID=int(input("\t Enter the depId=>"))
        EMPID=int(input("\t Enter the EmpId=>"))
        update.updatedata(ENAME,SALARY,DEPID,EMPID)
    elif(ch==4):
        EMPID=int(input("\t Enter the EmpId=>"))
        delete.deletedata(EMPID)
    else:
        print("\t Wrong choise")
    continue
