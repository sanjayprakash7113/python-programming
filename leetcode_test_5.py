digts=[1,2,3]
c=1
for i in range(len(digts)-1,-1,-1):
    digts[i]+=c
    if digts[i]>=10:
        digts[i]=0
        c=1
    else:
        c=0
        break
    if c==1:
        digts.insert(0,1)
print(digts)
