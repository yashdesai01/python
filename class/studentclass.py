class studentclass:
        def __init__(self):
                self.name=""
                self.rno=0
                self.m1=0
                self.m2=0
                self.m3=0
                self.total=0
                self.per=0
                self.grade=""
                
        def setstudent(s):
                s.rno=int(input("\t Enter roll=>"))
                s.name=input("\t Enter name=>")
                s.m1=int(input("\t Enter m1=>"))
                s.m2=int(input("\t Enter m2=>"))
                s.m3=int(input("\t Enter m3=>"))

        def caltotal(s):
                s.total=s.m1+s.m2+s.m3
                
        def calper(s):
                s.per=s.total/3

        def calgrade(s):
                if s.per>85:
                        s.grade="DIST"
                elif s.per>=75 and s.per<=85:
                        s.grade="A"
                elif s.per>=65 and s.per<=75:
                        s.grade="B"
                elif s.per>=55 and s.per<=65:
                        s.grade="c"
                elif s.per>=45 and s.per<=55:
                        s.grade="D"
                else:
                        s.grade="E"
                        
                
##        def getdetalis(self):
##                return self.name,self.rno,self.m1,self.m2,self.m3,self.total,self.per,self.grade

s=studentclass()
s.setstudent()
print("\t Roll no=>",s.rno,"name=>",s.name,"marks1=>",s.m1,"marks2=>",s.m2,"marks3=>",s.m3)
s.caltotal()
print("\t total=>",s.total)
s.calper()
print("\t per=>",s.per)
s.calgrade()
print("\t grade=>",s.grade)

##det=s.getdetalis()
##print(type(det))
##print("Name=>",det[0])
##print("Rollno=>",det[1])
##print("m1=>",det[2])
##print("m2=>",det[3])
##print("m3=>",det[4])
##print("total=>",det[5])
##print("per=>",det[6])
##print("grade=>",det[7])

