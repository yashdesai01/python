def sqr(x):
    return x*x

#without lambda function
lst=[3,4,5]
ans=list(map(sqr,lst))
print("without lambda function",ans)

#with lambda function
lst1=[6,7,8]
ans=list(map(lambda x:x*x,lst1))
print("with lambda function",ans)

