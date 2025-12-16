



#Used to repeat code over a sequence (list/tuple/string/range)
for i in [10,20,30]:
    print(i)

#range() – The Heart of Loops
#range(stop)
#range(start,stop)
#range(start,stop,step)

for i in range(5):
    print(i)
for i in range(1,4):
    print(i)
for i in range(10,0,-1):
    print(i)

#while loop – Runs Until Condition False

i=1

while i<=5:
    print(i)
    i=i+1

#break – Stop the Loop Immediately
    for i in range(1,10):
        if i==5:
            break
        #print(i)

#continue – Skip One Iteration
    for i in range(1,10):
        if i==3:
            continue
        print(i)
    


#pass – Placeholder (does nothing)
for x in range(5):
    pass


#Looping Over Different Collections
for i in [12,34]:
    print(i)
for i in (1,2,3):
    print(i)
for i in {1,2,3,4}:
    print(i)

#Dictionary – keys, values, items
d = {"a": 1, "b": 2}

for k in d:
    print(k)

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)


#loop patterns

#Sum of numbers
s=0
for i in range(1,6):
    s=s+i
    print(s) 

#Count items
    c=0
    for i in [1,2,3,1,0,5,0,0]:
        if i==0:
            c=c+1
print(c)


#Find maximum
a=[1,2,3,77]
b=a[0]
for i in a:
    if i>b:
        b=i
        print(i)



#Nested Loops
#A loop inside another loop.
for i in range(1,4):
    for j in range(1,7):
        print(i,j)















