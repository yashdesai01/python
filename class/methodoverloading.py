class operation:
    def add(s,no1,no2,no3=0):
        if(no3==0):
            return no1+no2
        else:
            return no1+no2+no3

oper=operation()
add=oper.add(3,5)
print("\t Addition of two number=>",add)
add=oper.add(3,5,6)
print("\t Addition of Three number=>",add)
