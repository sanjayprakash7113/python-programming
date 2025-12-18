#Default Arguments
#A default argument is a parameter that has a default value if the caller does not provide it.

def a(name="sanjay"):
    print(name)
a("frankenstain")
a() #yet sanjay not change

#Rules for Default Arguments
#Default arguments must come last in function definition.

#      def a(b=9,c):--error
#           print(b+c)
#      a(3,4)


def a(b,c=8):
    print(b+c)
a(3)


#Mixing Positional & Default Arguments(we can change the argument in the function when we call )
def a(b=9,c=2):
    print(b+c)
a(2,1)


#Mixing Positional + Keyword + Default
def a(b=9,c=7,d=3):
    print(b,c,d)
a(2,d=0)
a(4,3,9)
a(b=9,c=7)


#common error

#def test(a=5,b):
    #pass   # ❌ SyntaxError



#*args (Variable Length Positional Arguments)


#*args allows a function to accept any number of positional arguments
#Arguments are collected as a tuple

def a(*num):
    print(num)
a(1,2,3,4,5)

#*args in calculation
def a(*num):
    total=0
    for x in num:
        total=total+x
    return total
print(a(12,3,4,4,5,98))


#mix with normal parameters
def a(b,*num):
    print(b)
    print(num)
a(0,2,3,4,5,6,7,2,"e")


#Mix with Default Parameters
def demo(a, b=5, *args):
    print(a, b, args)
    print(b)

demo(1, 2, 3, 4)


#terating Over *args

def squ(*num):
    for i in num:
        print(i*i,end=" ")
squ(3,4,2)


#tricky question
def func(*args):
    print(args)

func(1)
func(1,2,3)




#If no extra arguments → args = () (empty tuple)
def calc(a, *args):
    print(a)
    print(args)

calc(5)
calc(5, 10, 15)





def total(*args):
    s = 0
    for x in args:
        s += x
        if x == 3:
            break
    print(s)

total(1,2,3,4,5)






def tricky(a, b=2, *args):
    print(a, b, args)

tricky(1)
tricky(1, 10, 20, 30)



def fun(*args):
    for i in args:
        for j in range(i):
            if j == 1:
                break
            print(i, j)
            
fun(2,3)



















