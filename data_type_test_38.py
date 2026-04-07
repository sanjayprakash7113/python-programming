s = "eceba"
k = 2

left = 0
mx = 0
d = {}

for i in range(len(s)):
    if s[i] in d:
        d[s[i]]+=1
    else:
        d[s[i]]=1
    while len(d)>k:
        d[s[left]]-=1
        if d[s[left]]==0:
            del d[s[left]]
        left+=1
    mx=max(mx,i-left+1)
print(mx)
