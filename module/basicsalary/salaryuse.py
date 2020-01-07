import hra
import da
import pf
import it
import gs
import netsalary

Eno=int(input("\t Enter the Eno=>"))
Ename=input("\t Enter the Ename=>")
bs=int(input("\n Enter the basic salary=>"))

HRA=hra.Hra(bs)
print("\t HRA=>",HRA)

DA=da.Da(bs)
print("\t DA=>",DA)

PF=pf.Pf(bs)
print("\t Pf=>",PF)

IT=it.It(bs)
print("\t IT=>",IT)

GS=gs.Gs(bs,HRA,DA)
print("\t GS=>",GS)

NETSALARY=netsalary.Netsalary(GS,PF,IT)
print("\n +=========================+")
print("\t  Eno=>",Eno)
print("\t  Name=>",Ename)
print("\t  Netsalary=>",NETSALARY)
print(" +=========================+")
