lang=["c","c++","java"]
script=[["php","python"],"javascript"]
print("lang=",lang)
print("script=",script)

print(lang==script)

script[1]="JAVASCRIPT"
print("script[0][1][1]=",script[0][1][1])

for lan in lang:
    print(lan)

program=lang+script
program.pop(0)
print("adding=>",program)
