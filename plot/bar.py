# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 23:28:18 2019

@author: yash
"""

import matplotlib.pylab as plt
import pandas as pd
empdata = {"emp_id":[1001,1002,1003,1004,1005,1006],"emp_sal":[10000,23000.50,18000.33,16500.50,12000.7,9999.99]} 

df=pd.DataFrame(empdata)

x=df['emp_id']
y=df['emp_sal']

plt.bar(x,y,label='Employee data',color='red')

plt.xlabel('Employee id')
plt.ylabel('Employee sal')

plt.title('MICROSOFT INC')
plt.legend()

plt.show()