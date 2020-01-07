import matplotlib.pylab as plt
slices=[50,20,15,15]
depts=["sales","production","HR","fiance"]
cols=["magenta","cyan","brown","gold"]
plt.pie(slices,labels=depts,colors=cols,startangle=90,explode=(0,0.2,0.1,0),shadow=True,autopct="%.1f%%")
plt.title("Shop")
plt.legend(bbox_to_anchor=(0,0))
plt.show()
