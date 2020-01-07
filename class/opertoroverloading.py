 class Num:
    def __init__(self,no=0):
        self.__no=no
    def getno(self):
        return self.no;
    def setno(self,no):
        self.__no=no
    def __add__(self,obj):
        new=Num()
        new.setno(self.getno()+obj.getno())
        return new
    def __sub__(self,obj):
        new=Num(self.getno()-obj.getno())
        return new

    def __mul__(self,*obj):
        ans=self.getno()
        for each in obj1:
            ans*=each.getno()
        new=Num(ans)
        return new

value="sarvaiya"
value1="yash"
con=value+value1
print("concate:-",con)

value=5
value1=9
add=value+value1
print("addition of two numbers:-",add)

obj=Num(5)
obj1=Num(4)
addobj=obj+obj1

print("\taddition of two object is",obj+obj1)
print("\taddition of two object is",addobj.getno())

print("\t subtraction of two object is",(obj-obj1).getno())

mulobj=obj*obj1*addobj*obj;
print("\t multipliation of three object is",mulobj.getNo())


