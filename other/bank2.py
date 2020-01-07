accNo = 0
name = ''
deposit=0
type = ''
alldata=[]
accountdata=[]
def NewAccount():
        accNo= int(input("\t Enter the account no : "))
        address=input("\t Enter the address : ")
        name = input("\t Enter the account holder name : ")
        type = input("\t Ente the type of account [C/S] : ")
        deposit = int(input("\t Enter The Initial amount(<4999 for current"))
        if(deposit<4999):
               deposit=int(input("\t Enter The Initial amount(<4999 for current"))
        
        print("\n\n\nAccount Created")
    
while ch != 6:
    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. EXIT")
    print("\tSelect Your Option (1-6) ")
    ch = input()
    
    if(ch==1):
        NewAccount()
    elif(ch==2):
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 1)
    elif(ch==3):
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 2)
    elif(ch==4):
        num = int(input("\tEnter The account No. : "))
        displaySp(num)
    elif(ch==5):
        displayAll();
    elif(ch==6):
        print("\tThanks for using bank managemnt system")
        break
    else :
        print("Invalid choice")
    ch = input("Enter your choice : ")
