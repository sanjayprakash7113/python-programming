a = [1, 2, 3, 4, 5, 6]
target = 7

left = 0
right = len(a) - 1
count = 0

while left < right:
    if a[left] + a[right] < target:
        count += (right - left)
        left += 1
    else:
        right -= 1

print(count)



aa = [1, 2, 3, 4, 6, 8]
target = 10

left = 0
right = len(a) - 1

while left < right:
    s = a[left] + a[right]

    if s == target:
        print((a[left], a[right]))
        break
    elif s < target:
        left += 1
    else:
        right -= 1





a = [1, 1, 2, 3, 4, 4, 5, 6]
b = []
for i in a:
    if i not in b:
        b.append(i)
target = 6
left = 0
right = len(b) - 1
while left < right:
    s = b[left] + b[right]
    if s == target:
        print((b[left], b[right]))
        break
    elif s < target:
        left += 1
    else:
        right -= 1


a = [3, 1, 4, 2, 5]
b=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if (a[i]+a[j])%2!=0 and j>i:
            b+=1
print(b)







