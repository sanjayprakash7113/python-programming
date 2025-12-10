#set not allow list,dic

#a={[1,2,3]}
#print(a)--error

#right way
s=set([1,2,3])
print(s)

#create empty set not this a={}--this is dictionary
a=set()
print(a)


#add
s={1,2,3,4}
s.add(2)
x=s.add(5)
print(s)
print(x)


#remove(if value not available showing error)
s={1,2,3,4}
s.remove(3)
#s.remove(5)--showing error
print(s)

#dicard(if value available remove it or not do not show error)
s={1,2,3,4}
s.discard(5)
s.discard(2)
print(s)

#pop (set is unorder so pop remove anything not last )
s={1,2,3,4}
s.pop()
print(s)

#clear remove all
s={1,2,3}
s.clear()
print(s)

#union
a={1,2,3}
b=[5,6,7]
print(a.union(b))
# print(a|b)--only in set not list 


#intersection
a={1,2,3,4}
b=[6,7,5,8]
print(a.intersection(b))
#print(a&b)--ojly work in set not list


a = {1, 2, 3}
b = {3, 4, 5}
c = [2, 5, 6]

result = a.union(b).intersection(c)
print(result)


#difference
a={1,2,3}
b=[4,5,6]
print(a.difference(b))

a={1,2,3}
b={4,5,6}
print(a-b)

#symmetric_difference()
a={1,2,3}
b=[4,5,6]
print(a.symmetric_difference(b))

a={1,2,3}
b={4,5,6}
print(a^b)

