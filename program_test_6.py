a = [56, 12, 89, 3, 45]
a.sort()
print(a[0])

b="python programming"
a="aeiou"
c=0
for i in b:
    if i.isalpha() and i.lower() not in a:
        c=c+1
print(c) 


s = "banana"
v=""
for i in s:
    if i!=v:
        v=i+v
print(v)


n=str(input())
if n==n[::-1]:
    print("pal")
else:
    print("no")

a = [2, 5, 8, 11, 14, 17]
b=0
for i in a:
    if i%2==0:
        b=b+int(i)
print(b)
