class Father:
    def __init__(self,height,color):
        self.height=height
        super().__init__(color)

    def setheight(self,height):
        self.height=height

    def getheight(self):
        return self.height

    def getvalue(self):
        print("Type ",type(self),"Value ",self)

class Mother:
    def __init__(self,color):
        self.color=color

    def setcolor(self,color):
        self.color=color

    def getcolor(self):
        return self.color

class child(Father,Mother):
    def __init__(self,prop,height,color):
        self.prop=prop
        super().__init__(height,color)
    def setproperty(self,prop):
        self.prop=prop
    def getproperty(self):
        return self.prop

p=int(input("\t Enter property=>"))
h=float(input("\t Enter height=>"))
c=input("\t Enter color=>")
ch=child(p,h,c)
print("\t height  =>",ch.getheight())
print("\t color   =>",ch.getcolor())
print("\t property=>",ch.getproperty())
##Father.getvalue(ch)
##ch.getvalue()
print(child.mro())    
