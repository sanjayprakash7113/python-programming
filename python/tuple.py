a=[1,2,3,4,5,6]
print(type(a))
print(a.append(123))
print(a)
q=tuple(a)
print(q)
print(type(a))
w=list(q)
print(w)
print(w.remove(1))
print(w)

a2=("sanjay","ashley","prakash","victor")
(x, *y, z) = a2
print(y)

