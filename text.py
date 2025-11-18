1 ) write a program to print the following patten
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


n=5
for i in range(1,n):
 for j in range(1,i+1):
     print(j,end=" ")





6) find if a number is prime or not
n=2
  if n<1:
    return False
  for i in range(2, int(n**0.5)+1):
        if n % i == 0:
    return False
  else:
    print(i)




2) check if a number is a special number. if sum of the digits plus product of the
digits plus product of the digits is equal to the original number.

n=123
b = 1
    digits = [int(d) for d in str(n)]
    total = sum(digits)
    for d in digits:
        b *= d
    a=total + b == n





4) Write a program that will take three digits from the user and add the square of each digit.
example (345 =(9+16+25 =50))

n=152
a = sum(int(d)**2 for d in n)
print(a)



3) Write a Python program that converts alternate letters of a string to uppercase.
(example use your full name)

a=["s","a","n","j","a","y"]
for i in a: 
 b=i[1:6:2]
print(b)
 c=b.uppercase()
 d=i[-1:-3]
f=b/d
print(f)



        

