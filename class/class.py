class person:
    def __init__(self):
        pass
    def setName(self,name):
        self.__name=name
    def setDOB(self,dob):
        self.__dob=dob
    def getName(self):
        return self.__name
    def getDOB(self):
        return self.__dob
    class dob:
        def __init__(self,day,month,year):
            self.__day=day
            self.__month=month
            self.__year=year
        def getall(self):
            return self.__day,self.__month,self.__year

name=input("\t Enter the Name=>")
day=int(input("\t Enter the day=>"))
month=int(input("\t Enter the month=>"))
year=int(input("\t Enter the year=>"))

##dob=person.dob(day,month,year)
##date=dob.getall()
##print("\t date of birth =>",date[0],"/",date[1],"/",date[2])


p=person()
p.setName(name)
dob=p.dob(day,month,year)
print("\t Name =>",p.getName())
date=dob.getall()
print("\t date of birth =>",date[0],"/",date[1],"/",date[2])

