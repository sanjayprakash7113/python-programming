def aa(a,b):
    print(a+b)
aa(2,4)

import math
print(math.sqrt(144))
print(math.factorial(4))
print(math.floor(6.9))
print(math.ceil(2.1))
print(math.pi)

import random
print(random.randint(1,10))
#print(random.choice["a","b","c"])--error
print(random.shuffle([1,2,3,4,5,99,999]))

import datetime
now=datetime.datetime.now()
print(now)
today=datetime.date.today()
print(today)


import os

print(os.getcwd())     # current working directory
#  os.mkdir("test_folder")---error---- # create folder
os.listdir()          # list files in current folder


import sys

print(sys.version)
print(sys.path)

import json

data = '{"a":1,"b":2}'
d = json.loads(data)      # string -> dict
print(d["a"])             # 1

s = json.dumps(d)         # dict -> string
print(s)                  # '{"a": 1, "b": 2}'



import time

print(time.time())# current timestamp
time.sleep(10)  # wait 2 seconds
print("done")









# from calc import add, sub

print(add(1,2))
print(sub(5,2))
