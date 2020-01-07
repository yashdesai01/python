import pandas as pd

edf=pd.read_excel("emp.xlsx","Sheet1",parse_dates=['doj'])
print(edf)

print("\n=>sort ascending order date wise\n")
asc=edf.sort_values('doj')
print(asc)

print("\n=>sort descending order date wise\n")
dec=edf.sort_values('doj',ascending=False)
print(dec)

print("\n=>multiple sorting\n")
mul_sort=edf.sort_values(by=["doj","sal"],ascending=[False,True])
print(mul_sort[["doj","sal"]])