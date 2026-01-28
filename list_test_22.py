a = [1, 2, 3, 4, 5]

odd = 0
even = 0

for i in a:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

count = odd * even
print(count)




a = [1, 1, 2, 2, 2, 3]

freq = {}
for x in a:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

count = 0
for v in freq.values():
    count += v * (v - 1) // 2
print(count)


a = [4, 4, 4, 2, 2]
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
c=0
for v in b.values():
    c+=v*(v-1)//2
print(c)


a=[1,2,3,4]
b=[]
for i in range(len(a)):
    if i==len(a)-1:
        b.append(a[0]*a[i])
    else:
        b.append(a[i]*a[i+1])
print(b)
