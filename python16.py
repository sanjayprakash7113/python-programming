num=int(input("enter the number:"))

if num>0:
    print(f"{num} this is positive number")
elif num<0:
    print(f"{num} this is negative number")
else:
    print("this is zero")


num1=int(input("enter the number 1:"))
num2=int(input("enter the number 2:"))
num3=int(input("enter the number 3:"))

if num1>num2 and num1>num3:
    print("num1 was grater value")
elif num2>num1 and num2>num3:
    print("num2 was grater value")
else:
    print("num3 was grater value")



what is the use of else if:

It is used when there are multiple conditions to check.
It avoids writing too many nested if statements and makes code cleaner




what is nested if:

An if statement inside another if is called a nested if.
It is used when one condition depends on another.



what is for loop:

A for loop is used when we know how many times the code should run

what is while loop

A while loop is used when we do not know the exact number of repetitions beforehand.




Difference between for and while loop with real-time examples

              For Loop 	                                                           While Loop
    When no. of iterations is known                                   	When iterations are unknown

    Printing first 10 numbers	                                         Read user input until they type "exit"





no = [10, 11, 12, 13]

for i in no:
    print(i)