a=[10,4,22,7]
b=sorted(a)
print(b[-1])


a="listen"
b="silent"
for i in a:
 for j in b:
   if i==j:
    print(True)


def a(n):
 if n <=1:
  return n
 return a(n-1) + a(n-2)
a(8)
	