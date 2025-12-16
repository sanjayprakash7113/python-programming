#A package = folder with modules inside
#Must contain a special file: __init__.py

#How to import from a package
from mypackage.calc import add
print(add(5,6))



from mypackage import calc
print(calc.add(3,4))



#Alias for package or module
import mypackage.calc as c
print(c.sub(5,2))



#import type
#from calc import add, sub
from calc import add,sub


#import module as m
import calc as c
import module as m



import numpy as np
import pandas as pd




#from module import * — IMPORT EVERYTHING (danger)

from cacl import *
print(add(1,2))
print(sub(3,1))


import cacl
cacl.add()
cacl.sub()



from cacl import add
add()










    
