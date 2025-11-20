a="education"
b="aeiou"
c=0
for i in a:
 for j in b:
  if i==j:
    c=c+1
print(c)


b="apple mango apple mango apple orange"
a=b.split()
fre={}
for i in a:
 fre[i]=fre.get(i,0)+1
print(fre)
   
a=[3,5,8,2,9,7]
b=sorted(a)
print(b[-2]) 



a=9
s=True
for i in range(2, int(a**0.5)+1):
 if a%i==0:
    print(False)
print(s)

a=[10,4,22,7]
b=sorted(a)
print(b[-1])


a="listen"
b="silent"
for i in a:
 for j in b:
   if i==j:
    print(True)




 