height = [1,8,6,2,5,4,8,3,7]
mx=0
for i in range(len(height)):
    for j in range(i+1,len(height)):
        mul=(min(height[i],height[j]))*(j-i)
        mx=max(mx,mul)
print(mx)
