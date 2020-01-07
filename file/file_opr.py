def add(no1,no2):
    return no1+no2

def sub(no1,no2):
    return no1-no2

def mul(no1,no2):
    return no1*no2

def div(no1,no2):
    return no1//no2

no=int(input("\t Enter the total of input=>"))
while(no<=3):
    try:
        file=open("demo.txt","a+")
        no1=int(input("\t Enter the number no1=>"))
        no2=int(input("\t Enter the number no2=>"))    
        print("\t =======MENU======")
        print("\t 1.ADD")
        print("\t 2.SUB")
        print("\t 3.MUL")
        print("\t 4.DIV")
        print("\t 5.MAX")
        print("\t 6.MIN")
        opt=int(input("\t Enter the Number=>"))
        if(opt==1):
            op="+"
            ans=add(no1,no2)
        elif(opt==2):
            op="-"
            ans=sub(no1,no2)
        elif(opt==3):
            op="*"
            ans=mul(no1,no2)
        elif(opt==4):
            op="/"
            ans=div(no1,no2)
        elif(opt==5):
            val=max(no1,no2)
            file.write(str(val)+"\n")
            file.seek(0)
            line=file.read()
            print(line)
            file.close()
        elif(opt==6):
            val=min(no1,no2)
            file.write(str(val)+"\n")
            file.seek(0)
            line=file.read()
            print(line)
            file.close()
        else:
            print("not")
            
        file.write("\n  %d %s %d = %d"%(no1,op,no2,ans)+"\n")
        file.seek(0)
        line=file.read()
        print(line)
        file.close()
    except ZeroDivisionError as ae: 
        print("Divide by zero")
    except ValueError:
        print("Invalid data for performming divison operation")
    except NameError:
        print("\t plz initialzed value")
    except Exception:
        print("\t Error")
    else:
        print("\t Done succesfully")
    continue
        
