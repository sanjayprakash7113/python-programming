class mobile():
 charger="b-type"  #classvariable
 def __init__(self):
  self.name=""    #instancevariable
  self.price=""
 def display(self):
  print(self.name)
  print(self.price)
  print(self.charger)

apple=mobile()
apple.name="i phone"
apple.price=115000
apple.display()
