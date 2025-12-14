#normal dic
d1={"a":1,"b":2,"c":3,"a":3}
print(d1)

#using dict
d2=dict(a=10,c=(1,2,3),d=("a","b"),e=[1,2,3],f={1,2,3,3})
print(d2)

d3=dict.fromkeys(['q','t'],(0,90))
print(d3)


#we add this even only "x" but  both at point the same list
d3=dict.fromkeys(["x","y"],[])
d3["x"].append(1)
print(d3)

#Key Immutability & Hashing
a={(1,2):[1,2,3,5]}
print(a)
#a={[1,2,3]:"victor"}--showng eror(we cannot use mutable in our key)


#access
a={"a":1,"b":2}
print(a["a"])
print(a.get("c"))#none (suspose key not available it was do not show error show none)

#update
a={"a":1,"b":2}
a["c"]=9
a["a"]=8,7
print(a)

#dictionary views
a={"a":1,"b":2,"c":3}
print(a.keys())
print(a.values())
print(list(a.items()))# we want we can change the data type
print("a" in a.keys())
print(2 in a.values())
print("a" in a)

#views is live (foucus on x)
d = {"x": 1, "y": 2}
x = d.keys()

d["z"] = 3

print(x)




#Iterating
for k in a.keys():
    print(k)
for k,v in a.items():
    print(k,v)

a={"a":1,"b":2,"c":3}
#remove the item
a.pop("a")
print(a)
#remove the last item
a.popitem()
print(a)
#set default item
d = {}
x = d.setdefault("k", [])
x.append(10)
print(d)

a.setdefault("c",8)
print(a)

a.update({"d":4,"a":8})
print(a)


#dictionary comprehension
# Basic
{x:x**2 for x in range(5)}  # {0:0,1:1,2:4,3:9,4:16}

# With condition
{x:x**2 for x in range(5) if x%2==0}  # {0:0,2:4,4:16}

# Nested dict comprehension
d = {i:{j:j*2 for j in range(3)} for i in range(2)}
# {0:{0:0,1:2,2:4},1:{0:0,1:2,2:4}}



#shallow copy
import copy

d1 = {'a':[1,2],'b':[3,4]}
d2 = d1.copy()               # shallow copy
d3 = copy.deepcopy(d1)       # deep copy

d2['a'].append(99)
print(d1['a'])   # [1,2,99]   <-- shallow copy shares inner list

d3['a'].append(100)
print(d1['a'])   # [1,2,99]   <-- deep copy independent




#nested copy trap
a = {"k":[1,2]}
b = a.copy()
b["k"] = b["k"] + [99]
print(a["k"])


#True, 1.0 all have same hash and compare equal:
d = {1:"x", True:"y", 1.0:"z"}
print(d)










