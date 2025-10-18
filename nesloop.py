
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

