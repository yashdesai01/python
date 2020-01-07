import mysql.connector

def displayALL():
    conn=mysql.connector.connect(host='localhost',database='world',user='root',password='')
    cursor=conn.cursor()
    cursor.execute("select * from emptab")
    try:
        allin=cursor.fetchall()
        for each in allin:
            print("\t",each)
        conn.commit()
    except:
        print("Error")
        conn.rollback()
    finally:
        conn.close()
        cursor.close()
