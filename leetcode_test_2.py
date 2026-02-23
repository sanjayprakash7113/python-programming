


nums = [0,0,1,1,1,2,2,3,3,4]

unique_pos = 0

for i in range(1, len(nums)):
    if nums[i] != nums[unique_pos]:
        unique_pos += 1
        nums[unique_pos] = nums[i]

# Replace remaining elements with "_"
for i in range(unique_pos+1, len(nums)):
    nums[i] = "_"

print(nums)


s ="Hello World"
s=s.split()
print(len(s[-1]))




a = [1,2,3,4,1]

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            print(True)
            exit()

print(False)

        
