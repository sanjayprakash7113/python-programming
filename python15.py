age=int(input("enter the age:"))
result=(input("higher sec result:"))

if age <=20 and result=="pass":
    print("you are eligible to college")
else:
    print("you are not eligible to college")


mark=int(input("enter the mark:"))
if mark>=95:
    print(f"{mark} :a++")
elif mark>=90:
    print(f"{mark} :b++")
elif mark>=85:
    print(f"{mark} :c++")
else:
    print(f"{mark} :d++")

temp=int(input("enter the temp:"))
if temp<=20:
    print(f"{temp}:cold")
elif temp>21 and temp<31:
    print(f"{temp}:normal")
elif temp>=31:
    print(f"{temp}:hot")


s1=input("enter the sub:")
s2=input("enter the sub:")
s3=input("enter the sub:")


avg=int(input("enter the avg:"))


if((s1 !=s2) and (s2 !=s3) and(s3 !=s1)) and s1 in("phy","chem","math") and s2 in("phy","chem","math") and s3 in("phy","chem","math") and avg>=99:
    print("doctor")
elif((s1 !=s2) and (s2 !=s3) and(s3 !=s1)) and s1 in("phy","chem","math") and s2 in("phy","chem","math") and s3 in("phy","chem","math") and  avg>=89:
    print("engineering")
elif((s1 !=s2) and (s2 !=s3) and(s3 !=s1)) and s1 in("phy","chem","math") and s2 in("phy","chem","math") and s3 in("phy","chem","math") and  avg>=79:
    print("arts")
else:
    print("comm")