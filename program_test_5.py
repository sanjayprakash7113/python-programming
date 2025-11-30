a="python"
b=""
for i in a:
    b=i+b
print(b)


a="hello world"
c=0
for i in a:
    b="aeiou"
    for j in b:
        if i==j:
            c=c+1
print(c)

a=[10, 25, 3, 99, 56]
a.sort()
print(a[-1])

n=str(573)
n.split(",")
a=int(n[0])
b=int(n[1])
d=int(n[2])
c=a+b+d
print(c)

a="level"
b=a[::-1]
if a==b:
    print("yes")


