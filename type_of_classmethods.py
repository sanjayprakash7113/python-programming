class lap():
 chargertype="c-type"
 def __init__(self):   
  self.brand=""
  self.price=34

 def getprice(self):
  print(self.price)

 @classmethod
 def changechargertype(cls):
  cls.chargertype="b-type"

 @staticmethod
 def info():
  print("this is os")
 

hp=lap()
hp.getprice()
hp.brand="iphone"
hp.changechargertype()

hp.info()  