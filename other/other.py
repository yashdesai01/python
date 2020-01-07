##mixed = [1, 2, 'a', 3, 4.0]
##a=[x**2 for x in mixed if type(x) == int]
##print(a)
##
monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5,
 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
print("The third month is " + monthNumbers[3])
dist = monthNumbers['Jan'] - monthNumbers['Apr']
print("Apr and Jan are", dist, "months apart")
keys = []
a=monthNumbers.keys()
print(a)
