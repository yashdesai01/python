import matplotlib.pylab as plt
sAge = [6,9,11,23,8,4,3,26,32,12,35]
bins = [0,5,10,15,20,25,30,35,40,45]
#histtype=barstacked or step or stepfilled or bar
plt.hist(sAge,bins,histtype="bar",rwidth=0.1,color='cyan',label="Students")
plt.xlabel("Age")
plt.ylabel("No of student")
plt.title("My university")
plt.legend()
plt.show()
