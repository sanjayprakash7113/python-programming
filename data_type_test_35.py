nums = [0,0,1,1,1,2,2,3,3,4]
left=0

for i in range(1,len(nums)):
    if nums[left]!=nums[i]:
        left+=1
        nums[left]=nums[i]
print(left+1)


nums = [0,1,0,3,12]
left=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[left]=nums[i]
        left+=1
for i in range(left,len(nums)):
    nums[i]=0
print(nums)


nums = [1,2,3,4,6,8,9]
target = 10
left=0
right=len(nums)-1
while left<right:
    pair=nums[left]+nums[right]
    if pair==target:
        print(left,right)
        break
    elif pair<target:
        right-=1
    else:
        left+=1



        
height = [5, 4, 3, 2, 100, 1, 100, 2, 3, 4, 5]
mx = 0
left = 0
right = len(height) - 1

while left<right:
    pair=(min(height[left],height[right]))*(right-left)
    mx=max(mx,pair)
    if height[left]<height[right]:
        left+=1
    else:
        right-=1
print(mx)


s = "madam"
left = 0
right = len(s) - 1

while left<right:
    if s[left]!=s[right]:
        print(False)
        break
    else:
        left+=1
        right-=1
else:
    print(True)
        

s = ["h","e","l","l","o"]
left=0
right=len(s)-1
while left<right:
    if s[left]!=s[right]:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    else:
        left+=1
        right-=1
print(s)






