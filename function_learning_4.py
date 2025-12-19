#Pure vs Impure Functions

                                 #pure
# Same input → same output
# No side effects

# No change to global variables
# No printing
# No input/output
# No file/database change

def a(a,b):
    return a+b
a(1,2)

def square(n):
    return n * n


                               #impure

#A function is IMPURE if any one of these is true:

#Uses Global Variable
x=10
def a():
    print(x)
a()

#Modifies Global Variable
x=5
def a():
    global x
    x=x-1
    print(x)
a()

#use print
def a(n):
    print(n)
a(2)






                             #RECURSION


#A function calling itself to solve a smaller version of the same problem

#Base Case---When to STOP

#Recursive Case---Call the same function with a smaller value


def num(n):
    if n==0:
        return
    num(n-1)
    print(n)
num(3)


def show(n):
    if n == 0:        # 🟥 BASE CASE (STOP)
        return
    print(n)
    show(n - 1)       # 🟦 RECURSIVE CALL

show(3)

def num(n):
    if n==0:
        return 0
    return n + num(n-1)
print(num(3))





#tricky
def f(n):
    if n <= 0:
        return 0
    return f(n-1)

print(f(3))


def g(n):
    if n == 0:
        return
    print(n)
    g(n-1)
    print(n)

g(2)



























