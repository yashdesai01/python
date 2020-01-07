import os
maxi = 20
cityFile = open("city.bin","wb+")
n= int(input("How Many Entries="))
for loop in range(n):
    city = input("Enter " + str(loop + 1) + " City Name: ")
    if(len(city) < 20):
        city = city + (maxi-len(city)) * ' '
        city = city.encode()
    cityFile.write(city)
cityFile.seek(0)
size = os.path.getsize("city.bin")
n = int(size/maxi)
while True:
    pos = 0
    cityFile.seek(0)
    print("1.Display All Record")
    print("2.Search City")
    print("3.Insert City")
    print("4.Delete City")
    print("5.Update City")
    print("6. Exit")
    ch = int(input("Enter Your Choice: "))
    if(ch == 1):
        for loop in range(n):
            data = cityFile.read(maxi)
            print(data.decode())
            pos+=maxi
            cityFile.seek(pos)
    elif(ch == 2):
        pos = 0
        found = False
        searchCity = input("Enter city name which you want to search=")
        for loop in range(n):
            name = cityFile.read(maxi)
            name = name.decode()
            if name.rstrip() .upper() == searchcity.upper():
                found = True
                print(name.rstrip(), "found on ",(loop+1) ,"position")
                break
            pos+=maxi
            cityFile.seek(pos)
        if found == False:
            print(searchCity , "not found")
    elif(ch == 3):
        name = input("Enter new city name=")
        cityFile.seek(0,2)
        if(len(name) <  20):
            name = name + (maxi - len(name)) * ' '
            name = name.encode()
            cityFile.write(name)
            n +=1
            print("No of Records:",n)
    elif(ch == 4):
        cityFile.seek(0)
        deleteCity = input("Which city do you want to delete..??")
        file2 = open("newfile.bin","wb")
        for loop in range(n):
            name = cityFile.read(maxi)
            name = name.decode()
            if name.rstrip().upper() !=deleteCity.upper():
                file2.write(name.encode())
            pos+=maxi
        cityFile.close()
        file2.close()
        os.remove("city.bin")
        os.rename("newfile.bin","city.bin")
        cityFile = open("city.bin","rb+")
        size = os.path.getsize("city.bin")
        n = int(size/maxi)
    elif(ch == 5):
        found = False
        pos=0
        oldName = input("Enter old City Name=")
        newName = input("Enter New City Name=")
        if(len(newName) < 20 ):
            newName = newName + (maxi - len(newName)) * '  '
        if(len(oldName) < 20 ):
            oldName = oldName + (maxi - len(oldName)) * '  '
        for loop in range(n):
            cityFile.seek(pos)
            name = cityFile.read(maxi)
            name = name.decode()
            if oldName.upper() == name.upper():
                found = True
                cityFile.seek(-20,1)
                cityFile.write(newName.encode())
            pos+=maxi
        if found==True:
            print("Records Update Successfully:")
        else:
            print("No records found:")
    elif (ch == 6):
        break
cityFile.close()
            
