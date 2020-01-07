import mysql.connector

def updatedata(ENAME,SALARY,DEPID,EMPID):
        conn=mysql.connector.connect(host='localhost',database='world',user='root',password='')
        cursor=conn.cursor()
        qry="update `emptab` set `empName`='%s',`salary`='%d',`depID`='%d' where empId='%d'" 
        try:
            cursor.execute(qry%(ENAME,SALARY,DEPID,EMPID))
            conn.commit()
        except:
            print("Error")
            conn.rollback()
        finally:
            conn.close()
            cursor.close()
