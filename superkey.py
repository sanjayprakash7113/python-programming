class a():
 def __init__(self):
  print("a")

class b():
 def __init__(self):
  super().__init__()
  print("b")
 
class c(a,b):
 def __init__(self):
  super().__init__()
  print("c")

obj=c()


 


