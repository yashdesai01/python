def odd(lst):
    lstodd=[]
    for each in lst:
        if each%2 != 0:
            yield each
#with use list
ans=list(odd([10,15,17,20,25]))

#without use list
#ans=odd([10,15,17,20,25])
print(type(ans))
for each in ans:
    print(each)
