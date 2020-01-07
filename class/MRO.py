class Father:
    def __init__(self,x):
        self.x=x
    def getproperty(self):
        return self.x

class son(Father):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y
    def getproperty(self):
        return super().getproperty()+self.x

x=int(input("\t Entet Father =>"))
y=int(input("\t Enter son    =>"))
s=son(x,y)
print("\t Property = ",s.getproperty())
print(son.mro())
