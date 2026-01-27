a = [2, 5, 1, 4, 3]
b=0
for i in range(len(a)):
    for j in range(1,len(a)):
        if i<j and a[i]>a[j]:
            b+=1
print(b)


a = [4, 2, 6, 1, 3, 5]
b=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if i<j and a[i]<a[j] and a[i]%2==0 and a[j]%2==0:
            b+=1
        else:
            if i<j and a[i]<a[j] and a[i]%2!=0 and a[j]%2!=0:
                b+=1
            else:
                pass
print(b)


a = [3, 1, 4, 2, 5, 6]
b=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if i<j and a[i]<a[j] and a[i]!= a[j] and a[i]*a[j]%3==0:
            b+=1
print(b)





a = [1, 2, 3, 4, 5, 6]
b = 0

for i in range(len(a)):
    for j in range(i+1, len(a)):
        c = a[i] + a[j]

        if c < 2:
            continue

        prime = True
        for k in range(2,c):
            if c % k == 0:
                prime = False
                break

        if prime:
            b += 1

print(b)






















                                 
