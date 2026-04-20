n=24
if n%2==1:
    print("Weird")
elif n%2==0 and n>=2 and n<=5:
    print("Not Weird")
elif n%2==0 and n>=6 and n<=20:
    print("Weird")
elif n>20:
    print("Not Weird")


print(4/3)

n = 5
for i in range(n):
    print(i*i,end=" ")
print()


time="09:30"
token="a@1"
hour=int(time[0:2])
first=token[0]
last=token[2]

if 12>hour:
    if first.isalpha() and last.isdigit():
        print("valid")
    else:
        print("invlid")
else:
    if 12<hour:
        if first.isalpha() and last.isdigit():
            print("valid")
        else:
            print("invalid")
