
class Lib:
    def __init__(self, name, password, id, book_name, book_id):
        self.name = name
        self.__password = password
        self.__id = id
        self.book_name = book_name
        self.book_id = book_id
        print("You are a member")
    def show(self):
        return self.__password, self.__id
    def change(self, new_pass, new_id):
        self.__password = new_pass
        self.__id = new_id
    def p_int(self):
        print(self.name, self.book_name, self.book_id)
p1 = Lib("victor", "abc123", "007", "The Magic of Thinking Big", "7112")

p1.p_int()
print(p1.show())



from abc import ABC,abstractmethod
class deposit(ABC):
 @abstractmethod
 def account_no(self):
    pass
 @abstractmethod
 def account_nmae(self):
    pass
 @abstractmethod
 def amount(self):
    pass
 def pan(self):
    pass

class account(deposit):  
 def account_no(self):
    print("account number pass") 
 def account_nmae(self):
    print("victor") 
 def amount(self):
    print(20,00000)
 def date(self):
   print(10/10/12025)

a1=account()
print(a1)
print(a1.amount())
print(a1.account_no)










    
    