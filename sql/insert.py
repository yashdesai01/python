import mysql.connector

def insertdata(ENAME,SALARY,DEPID):
        conn=mysql.connector.connect(host='localhost',database='world',user='root',password='')
        cursor=conn.cursor()
        qry="insert into `emptab` (`empName`,`salary`,`depID`) values ('%s','%d','%d')"
        try:
            cursor.execute(qry%(ENAME,SALARY,DEPID))
            conn.commit()
        except:
            print("Error")
            conn.rollback()
        finally:
            conn.close()
            cursor.close()
