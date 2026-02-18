height = [1,8,6,2,5,4,8,3,7]
a=0
for i in range(len(height)):
    for j in range(i+1,len(height)):
        res=height[j]-height[i]
        if res>a:
            a=res
print(a*a)
