s="hello"
r=""
for i in s:
    r=i+r
print(r)


s = "madam"
p=""
for i in s:
    p=i+p
if p==s:
    print(True)
else:
    print(False)


s = "hello world"
v="aeiou"
vc=0
cha=0
for i in s:
    if i in v:
        vc+=1
    cha+=1

        
print(cha)
print(vc)


s1 = "listen"
s2 = "silent"

if sorted(s1)==sorted(s2):
    print(True)
else:
    print(False)





s = "abcabcb"
mx=0
for i in range(len(s)):
    cur=""
    for j in range(i,len(s)):
        if s[j] not in cur:
            cur+=s[j]
            if len(cur)>mx:
                mx=len(cur)
            else:
                break
             
print(mx)
        
        
    






