a = [1, -2, 3, -4, 5]
negatives = []
positives = []

for i in a:
    if i < 0:
        negatives.append(i)
    else:
        positives.append(i)
print(negatives + positives)



a = [1, 2, 3, 4, 5, 1]

sorted_flag = True

for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        sorted_flag = False
        break

print(sorted_flag)

a=[1, 2, 3, 1, 2, 3, 4, 0]
b=a[0]
c=[]
d=[]
for i in a:
    if i>b:
        c.append(i)
    else:
        b=i
for k in c:
    if k not in d:
        d.append(k)
print(d)



a=[1,2,3,4,5,6]
b=[]
for i in range(len(a)):
    if i==0:
        left=0
    else:
        left=a[i-1]
    if i==len(a)-1:
        right=0
    else:
        right=a[i+1]

    b.append(left+right)
print(b)


a= [3, 7, 2, 9, 4,8]
m=0
s=0

for i in a:
    if i>m:
        s=m
        m=i
    elif i != s and i>s:
        s=i
print(i)





a=[1,2,3,4,5,6]
b=[]
for i in range(len(a)-2,len(a)):
    b.append(a[i])
for i in range(len(a)-2):
    b.append(a[i])
print(b)
      


        
        






































