n = int(input())
num = int(input())
chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res=""
while num>0:
    rem=num%n
    res=chars[rem]+res
    num=num//n
print(res)
    
num1=list(map(int,input().split()))
num2=list(map(int,input().split()))
print(num1)
