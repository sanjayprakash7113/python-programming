# it was slow chech one by one 
l=[1,2,3,4]
print(7 in l)

# it was faster jump directly into the value
s={1,2,3,4}
print(1 in s)

print(hash("FB") == hash("Ea"))



s1 = {1,2,3}
s2 = s1.copy()

s2.add(4)

print(s1)   # {1,2,3}
print(s2)   # {1,2,3,4}


import copy
s3=copy.deepcopy(s1)

#shollow copy == deep copy(we do n ot need deep copy because both are same in set) 
