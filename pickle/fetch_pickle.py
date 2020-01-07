import emp
import pickle

f=open("Empbin.dat","rb")
while(True):
    try:
        obj=pickle.load(f)
        obj.getALL()
    except Exception as ex:
        print(ex)
        break
f.close()
