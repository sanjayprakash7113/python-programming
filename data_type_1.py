a=[1,2,3,4]
b=[]
for i in a:
    if i%2==0:
        b.append(i*i)
    else:
        b.append(i+1)
print(b)


time="12:00"
token="a@1"
hour=int(time[0:2])
first=token[0]
last=token[2]

if hour<=12:
    if first.isalpha() and last.isdigit():
        print("valit")
    else:
        print("invalit")
else:
    if first.isdigit() and last.isalpha():
        print("valit")
    else:
        print("invalit")
        
        
a = [5, 15, 50]
b = ["C1", "C2", "C3"]
w = 30

for i,j in zip(a,b):
    if i < w:
        print(j, end=" ")


values = {'r':4, 'w':2, 'x':1, '-':0}
a="rwxrwxrwx"
res=""
for i in range(0,len(a),3):
    cur=0
    for j in range(i,i+3):
        cur+=values[a[j]]
    res+=str(cur)
print(res,end=" ")



def count(s):
    if not s or s[0]=="0":
        return 0
    n=len(s)
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        if s[i-1]!="0":
            dp[i]+=dp[i-1]
        two=int(s[i-2:i])
        if 10<=two<=26:
            dp[i]+=dp[i-2]
    print(dp[n])

count("226")



def prim(s):
    if s<2:
        return False
    for i in range(2,s):
        if s%i==0:
            return False
    return True
def is_prim(n):
    for a in range(2,n):
        b=n-a
        if prim(a) and prim(b):
            print(a,b)
            return
a=int(input())
is_prim(a)
    





