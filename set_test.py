a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6,7]
c=set(a)
d=set(b)
print(c&d)


a = [1, 2, 3, 4, 5, 2]
c=set()
b=set()
for i in a:
    if i not in b:
        b.add(i)
    else:
        c.add(i)
print(c)
        

    
a = [1, 2, 3]
b = [3, 4, 5]
q=set(a)
c=set(b)
d=q|c
print(d)




a = [10, 20, 30, 40]
b = [30, 40, 50, 60]
c=set(a)
d=set(b)
print(c&d)



a = [7, 8, 9, 7, 10]
b=set(a)
if len(a)==len(b):
    print(False)
else:
    print(True)



a = [1, 2, 3, 4, 5]
b = [2, 4]
c=set(a)
d=set(b)
print(c-d)




a = [4, 5, 6, 4, 7, 5, 8]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

a = [1, 2, 3, 4, 5, 6]
b=[]
c=[]
e=set()
for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
d=c+b
print(d)




a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c=set(a)
d=set(b)
e=c-d
f=d-c
print(e|f)


a = [1, 2, 3, 2, 4, 5, 1, 6, 5]
b=set()
c=set()
for i in a:
    if i not in b:
        b.add(i)
    else:
        c.add(i)
print(c)

a = [1, 2, 4, 6, 7, 9]
b=set()
for i in a:
    if i-1 not in a and i+1 not in a:
        b.add(i)
print(b)


a = [1, 2, 2, 3, 4, 4, 5]
seen = set()
unique = set()

for x in a:
    if x not in seen:
        seen.add(x)
        unique.add(x)
    else:
        if x in unique:
            unique.remove(x)  
print(unique)
























        




