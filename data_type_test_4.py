s = "pwwkew"

seen = {}
left = 0
max_len = 0

for right in range(len(s)):
    if s[right] in seen and seen[s[right]] >= left:
        left = seen[s[right]] + 1

    seen[s[right]] = right
    max_len = max(max_len, right - left + 1)

print(max_len)


nums = [4, 3, 2, 7, 8, 2, 3, 1]
b={}
for i in nums:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
b=[]
for k,v in b.items():
    if v>i:
        b.append(k)
print(b)
