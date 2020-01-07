def fun(no):
    suma=0
    for each in no:
        suma=suma+each
    return suma

no=input("Enter the number")
nos=no.split()
lst=[int(x) for x in nos]
print(lst)
ans=fun(lst)
print("sum=>",ans)
