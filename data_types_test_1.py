words = ["apple", "hi", "banana", "cat", "python"]
k = 3
a=0

for i in words:
    if len(i)>k:
        a+=1

print(a)

s = "programming"
b={}
c=0
for i in s:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
for i in b.values():
    if i>1:
        c+=1
print(c)


words = ["apple", "banana", "orange", "umbrella", "sky", "ice"]
b="aeiou"
a=0
for i in words:
    for j in b:
        if i.startswith(j):
            a+=1
print(a)


nums = [1, 3, 2, 1, 4, 1, 3]
b={}
for i in nums:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
c=0
a=None
for k,v in b.items():
    if v>c:
        c=v
        a=k
print(a)
        







