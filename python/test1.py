
1) Write a Program to extract each digit from an integer in the reverse order

a=[21,23,43,54,56,78,76]
print(a.reverse())
print(a)

output:[76, 78, 56, 54, 43, 23, 21]

2)Accept any three string from one input()
call and split into 3
difference stringand display it.

b,c,d=input("enter the value :").split()
print(b)
print(c)
print(d)

output:enter the value :w e r
w
e
r

3)Return the count of a given substring from a string

sen =("radha is most beutiful,radha is queen of vraj,radha is most beloved to govind")
print(sen.count("radha"))

output:3



4) Print characters from a string that are present at an even index number Write a program to
accept a string from the user and display characters that are present at an even index number.

name=("sanjay prakash")
print(name[0:15:2])

output:sna rks

6)  Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
print(dict1.update(dict2))
print(dict1)

output:{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


7) Write a Python program to change Brad’s
salary to 8500 in the following dictionary.

sample_dict = { 'emp1': {'name': 'Jhon', 'salary': 7500},
'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3':
{'name': 'Brad', 'salary': 500} }

sample_dict["emp3"]["salary"]=8500
print(sample_dict)

output:output:{'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3': {'name': 'Brad', 'salary': 8500}}


8) The given tuple is a nested tuple. write a
Python program to print the value 20.

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

output:20

9) Write a program to unpack the following tuple into four variables and display each variable.

tuple1 = (10, 20, 30, 40)
(a,b,c,d)=tuple1
print(a)
print(b)
print(c)
print(d)

output:
10
20
30
40