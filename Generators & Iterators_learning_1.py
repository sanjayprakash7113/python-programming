                                   #iterator

#An iterator is an object that:,--Gives one value at a time,--Remembers where it stopped
b=[1,21,3]
b=(1,2,3)
a=iter(b)
print(next(a))
print(next(a))
print(next(a))

#print(next(a))--error happen becaues without element

#What iter() and next() Do
#iter() → creates iterator,
#next() → gives next value

for i in [1,2,30]:
    print(i)

    
a=iter([1,2,3])
print(next(a))
print(next(a))
print(next(a))

#for loop = iter() + next() (internally)





                               #generators

# A generator is a function that returns values one-by-one
# It uses the keyword yield instead of return

#Normal function vs Generator

def num():
    return 999
    return 777
print(num())
#This does NOT work (function stops at first return)


def n():
    yield 1
    yield 2
    yield 3
a=n()
print(next(a))
print(next(a))
print(next(a))
#Returns values one at a time

                     #How Generator Works (Internally)
#When function is called → it does NOT run,--It returns a generator object
#Code runs only when next() is called.--State is remembered


def gen():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")



a=gen()
print(next(a))
print(next(a))


def test():
    yield 1
    yield 2

t = test()
print(next(t))
print(next(t))
# print(next(t))--error like iterator



                            #GENERATOR vs LIST
#All values are created at once---Stored fully in memory

nums = [x for x in range(5)]
print(nums)


#Generator (Lazy Evaluation)
nums = (x for x in range(5))
print(nums)

#Values created one-by-one--Stored only when needed


#Regex = Regular Expression
#It is a pattern used to find, match, or validate text










      

























