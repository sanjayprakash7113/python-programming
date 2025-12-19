#**kwargs (Keyword Variable Arguments)

#**kwargs collects keyword arguments,,,Stored as a dictionary
#Keys = parameter names,,,Values = argument values

def a(**num):
    print(num)
a(a=10,b=30)


#Iterating over **kwargs
def a(**num):
    for k,v in num.items():
        print(k,v)
a(name="victor",age=98)


#Mixing Parameters (STRICT ORDER RULE)
#correct order
def a(b=0,c=0,*num,**name):
    print(b,c,num,name)
a(2,3,4,5,3,1,"victor")
a(name="god")


         #wrong order
#def func(**kwargs, *args):
    #pass  # SyntaxError

#positional → default → *args → **kwargs





#Mixing All Types (Real Example)

def demo(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

demo(1, 2, 3, x=10, y=20)



#tricky question
def f(**kwargs):
    print(kwargs)

#f(1, 2)--type error



                        #Local vs Global Scope (EXPERT LEVEL)
#Scope = where a variable is accessible

#Global Variable
#A variable created outside all functions

x=10 #global
def a():
    print(x)
a()



#local variable
#A variable created inside a function.

def a():
    c=0
    print(c)
a()
# print(c)---  we can not access local variable inside the class




#Local Shadows Global (VERY IMPORTANT)
x=9
def num():
    x=7
    print(x) 
num()
print(x) #global variable print this time



#global Keyword (Dangerous but Powerful)
#Used when you want to modify a global variable inside a function.
x=8
def a():
    global x
    x=1231
    print(x)

a()
print(x)





#Reading vs Writing Global Variables (TRAP)
x=10
def a():
    print(x)
a() #reading is ok 



x = 10

def test():
    x = x + 1
    print(x)

# test()--error
#UnboundLocalError: local variable 'x' referenced before assignment


#fixing with global

x=999
def a():
    global x
    print(x)
    x=x+1
    print(x)
a()


#tricky question
x = 5

def fun():
    print(x)
    x = 10

#fun()--error



#inner() prints nearest scope x → 20
x = 10

def outer():
    x = 20
    def inner():
        print(x)
    inner()

outer()
print(x)
















    











































    



