
course=input("enter the course:").lower()
sub=input("enter the sub:").lower()

if sub=="python":
 if course=="da":
    print("student da:fees:40k")
 elif course=="pfs":
    print("student pfs: fees:45k")
 else:
    print("student ds:fees:32k")
else:
    print("student is not python")




age=int(input("enter the age:"))
country=input("enter the country:")

if age>=18:
 if country=="india":
    print("you can eligible to vote")
 elif country !="india":
    print("you eligible to vote but not in india")
else:
    print("you can not vote")
