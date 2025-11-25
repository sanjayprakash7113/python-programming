class goe:
 name=""
 drink=""
 def party(self):
    print("lets party")
 def beach(self):
    print("enjoying beach")
ram=goe():
sam=goe():

print(ram.party())

ram.name="ram"
print(ram.name)
sam.name="sam"
print(sam.name)

ram.drink="yes"
sam.drink="over drink"
print(ram.drink)
