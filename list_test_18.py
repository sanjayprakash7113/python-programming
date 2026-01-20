a = [1, 2, 3, 4, 5]
b=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if (a[i]+a[j])%2!=0 and i<j:
            b+=1
print(b)


a=[2,4,7,9,10]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]%2==0 and a[j]%2==0:
            if (a[i]-a[j])%2==0 and i<j:
                print((a[i],a[j]))
        else:
            if a[i]%2!=0 and a[j]%2!=0:
                if (a[i]-a[j])%2==0 and i<j:
                    print((a[i],a[j]))
            else:
                pass

a = [1, 2, 3, 4, 6]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if (a[i]*a[j])%3==0 and j>i:
            print((a[i],a[j]))

a = [1, 2, 3, 4, 5, 6]
t = 7
c=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if (a[i]+a[j])>t:
            c+=1
print(c)



