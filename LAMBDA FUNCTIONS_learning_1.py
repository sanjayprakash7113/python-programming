# A lambda is a small, anonymous function
# Written in one line


#No return keyword
#Expression result is returned automatically


#Lambda Syntax
# lambda arguments : expression
# No return keyword,Expression result is returned automatically


s=lambda a,b: a+b
print(s(3,4))
e=lambda a:a*a
print(e(4))
f=lambda a:a%2==0
print(f(6))


                                                 #map

#map() is used to apply a function to each item in a sequence.
# map(function,iterable)

#key Points About map()--2.Returns a map object,
#3.Convert to list() to see output.4.Does not modify original list


def squ(x):
    return x*x
print(list(map(squ,[12,13,15])))

print(list(map(lambda x:x*x,[4,5,6,7,8])))


nums = [1, 2, 3]
result = map(lambda x: x * 3, nums)
print(nums)
print(list(result))



                                  #filter()



# filter() selects elements from a sequence
# Keeps only items where condition is True


#syntex
#map(function,iterable)


#function must return true/false
#return filter object

n=[1,2,3,4,5]

print(list(filter(lambda x:x%3==0,n)))


nums = [0, 1, "", "hi", None, 5]
print(list(filter(None, nums)))

#LOCK THIS RULE FOREVER

#filter(None, iterable)

#removes all falsy values
# keeps only truthy values
#Falsy values in Python:
  #0,"" (empty string),None,False



                       #reduce
#reduce = keep combining until one value remains
#reduce() reduces a list to a single value
#It applies a function cumulatively



# it was not build-in like map and reduce
from functools import reduce


#syntex
#reduce(function, iterable)



from functools import reduce
a=reduce(lambda a,b:a+b,[1,2,3,4])
print(a)


print(reduce(lambda a, b: a if a > b else b, [3, 7, 2, 9]))

print(reduce(lambda a, b: a + b, [1, 2, 3], 10))



#reduce(lambda a, b: a + b, [])
# TypeError



reduce(lambda a, b: a + b, [], 5)
# returns 5










































