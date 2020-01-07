import mysql.connector
def deletedata(EMPID):
        conn=mysql.connector.connect(host='localhost',database='world',user='root',password='')
        cursor=conn.cursor()
        qry="delete from `emptab` where empId='%d'" 
        try:
            cursor.execute(qry%(EMPID))
            conn.commit()
        except:
            print("Error")
            conn.rollback()
        finally:
            conn.close()
            cursor.close()
