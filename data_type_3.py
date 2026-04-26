ch = input()
print(ord(ch))


num=323-1
c=0
for i in str(num):
    if i!="-":
        c+=1
print(c)



arr = ["pass", "sas", "asps", "df"]
num=0
for i in arr:
    if i[::-1]==i:
        pass
    else:
        num+=1
print(num)
        

n="\d\"
print(len(n))
