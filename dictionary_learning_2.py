#Merge Dictionaries in Python

#update
a1={"a":1,"b":2}
a2={"b":30,"c":5}
a1.update(a2)
print(a1)

#Using {**d1, **d2} (Unpacking)
a1={"a":1,"b":2}
a2={"b":21,"c":4}
a3={**a1,**a2}
print(a3)

#Using | operator
a1={"a":1,"b":2}
a2={"b":56,"c":566}
a3=a1|a2
print(a3)
print(a1|a2)


#Nested Dictionary Merge (Tricky)
a1={"a":{"x":2},"b":3}
a2={"a":{"y":4},"c":67}
a3={**a1,**a2}
print(a3)
print(a1["a"])
print(a2["a"])


#Sorting Dictionaries in Python


#sort by KEYS
a={"c":1,"b":7,"a":4}
a1=dict(sorted(a.items()))
a2=dict(sorted(a.items(),reverse=True))
print(a1)
print(a2)

#Sort by VALUES
a2=dict(sorted(a.items(),key=lambda x:x[1]))
a3=dict(sorted(a.items(),key=lambda x:x[1],reverse=True))
print(a3)
print(a2)

#Sort Nested Dictionaries

d={
    "a":{"age":20},
    "b":{"age":10},
    "c":{"age":40}
    }

d1=dict(sorted(d.items(),key=lambda x:x[1]["age"]))
print(d1)






#CREATE NESTED DICTIONARIES

student={"name":"victor",
         "marks":{"math":100,
                  "socila":100}}

#ACCESS DEEP VALUES
a=student["marks"]["math"]
print(a)

#ADD / UPDATE INSIDE NESTED DICTS
student["marks"]["science"]=99
print(student)
student["add"]={"pincode":621777,"city":"chenna"}
print(student)






#.setdefault() DEEP TRICK
order={}
order.setdefault("item",[]).append("milk")
order.setdefault("item",[]).append("cake")
print(order)



#NESTED MUTATION TRAPS

#Shared nested objects

data = {"a": [], "b": []}

data["a"].append(10)
data["b"].append(20)
data = {"x": [0] * 3}
print(data)

#Using same inner dict accidentally
inner = {"value": 1}
print(inner)
d = {"a": inner, "b": inner}
d["a"]["value"] = 99
print(inner)

d = {"a": {}}
d["a"].setdefault("marks", []).extend([1,2,3])
d["a"].setdefault("marks", []).append(4)
print(d)

t = {"a": {"b": {"c": 10}}}
print(t["a"]["b"]["c"])





#JSON & Python Dictionary

#Convert JSON → Python dict
import json
s='{"a":1,"b":4,"c":[1,2,3]}'
d=json.loads(s)
print(d)

#Convert Python dict → JSON
import json
a={"a":1,"b":2,"c":[1,2,3]}
s=json.dumps(a)
print(s)
