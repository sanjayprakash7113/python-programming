num=int(input("enter the number:"))

if num%2==0:
    print(f"this is even number: {num}")
else:
    print(f"this is add number: {num}")



num1=int(input("enter the number:"))

if num1>0:
    print(f"this is positive value: {num1}")
else:
    print(f"this is negative value: {num1}")


num2=int(input("enter the number:"))

if num2%5==0 or num2%7==0:
    print(f"this is divisble by five or seven: {num2}")

else:
    print(f"this is some of numbers: {num2}")



num3=int(input("enter the number:"))

if num3%2==0 and num3%3==0:
    print(f"this is divisble by two and three: {num3}")

else:
    print(f"it is not divisble by two and three: {num3}")


user=input("enter the user name:")
password=int(input("enter the password:"))

if user=="sla" and password=="1234":
    print("you have access")
elif user=="sla" and password!="1234":
    print("your password wrong")
elif user!="sla" and password=="1234":
    print("your user name wrong")
else:
    print("you did not have a access check your username and password")









