gmail=input("")
if "@" in gmail and gmail.endswith("@gmail.com") and " " not in gmail:
    print("valid email")
else:
    print("not valid email")


current_password=7112003
current_username="victor"


username=input("enter your username",)
password=input("enter your password",)

if current_username==username and current_password==password:
    print("you have a access")
elif current_username==username and current_password!=password:
    print("you password incorrect")
elif current_username!=username and current_password==password:
    print("your user name was incorrect")
else:
    print("invalid")


n=10
a=1
for i in range(n):
    print(a,end=" ")
    a=a*2


b=2468
n=b
a=0
even=True
while n>0:
    c=n%10
    if c%2!=0:
        even=False
        break
    n=n//10
if even:
    print("even")
else:
    print("not even")
        
        
