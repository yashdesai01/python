string=input("\t Enter your name")
index=0

while(index<len(string)):
    print(string[index],end="")
    index=index+1

search=input("\n\tenter searching character")
index=0
count=0

while(index<len(string)):
    if(string[index]==search):
        count=count+1
        index=index+1

print("\n Search char apper",count,"time")
search.count(search)
