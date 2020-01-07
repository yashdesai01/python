import pandas as pd
import xlrd
edf = pd.read_excel("emp.xlsx","Sheet1")
print(edf)
rows,cols=edf.shape

#print rows,cols
print("rows=>",rows)
print("cols=>",cols)

#paticular column data print
print("Emp Id,Emp Name and salary")
data1=edf[["empid","ename","sal"]]
print(data1)

#maximum salary
print("Maximum salary")
max_salary=edf['sal'].max()
print(max_salary)

#minimum salary
print("Minimum salary")
max_salary=edf['sal'].min()
print(max_salary)

#print("Retrive columns based on single condition")
data_sal=edf[edf.sal>10000]
print(data_sal)
#
#print("Rerive the selected colums based on multiple condition")
data_con=edf[["ename","sal"]][(edf.dep=="PHP") | (edf.dep=="Java")]
print(data_con)

#filter data
filt=["PHP","Java"]
filt_data=edf[["ename","sal"]][edf.dep.isin(filt)]
print(filt_data)

#speife index empid
print("setting column index")
index_data=edf.set_index('empid')
print(index_data)

#print("Retrive selected colums based on multiple condition")
data=edf[["ename","sal"]][edf.dep=="Java"]
data1=data[data.sal==data.sal.min()]
print(data1)
#
#print("Reset index")
edf.reset_index(inplace=True)
print(edf)
print(type(max_salary))
print(type(data))
