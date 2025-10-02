s1={"name":"sanjay","age":20,"name":"prakash"}
print(s1["age"])
print(s1.keys())
print(s1.values())
print(s1.items())
print(s1.get("name"))
s2={"id":1,"class":"student"}
print(s1.update(s2))
print(s1)
print(s1.pop("name"))
print(s1)

s2=s1.copy()
print(s1)

s1["hr"]="victor"

print(s1)

print("victor" in s1.values())

a1={"name":["a","b","f","r"],"id":[1,2,3,4,5],"class":["a1","b1","c1"]}
print(a1.items())
a1["name"][1]="victor"
print(a1)








