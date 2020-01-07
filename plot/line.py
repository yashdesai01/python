# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 04:27:03 2019

@author: yash
"""

import matplotlib.pylab as plt

years=['2012','2013','2014','2015','2016','2017']
profits=[9,10,10.5,8.8,10.9,9.75]

plt.plot(years,profits,'blue')

plt.title('YASH COMPANY')

plt.xlabel('Years')
plt.ylabel('Profits in million Rs')

plt.show()