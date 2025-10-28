class teacher():
 def mark(self):
    self.__student_mark=34
    self.__student_name="victor"

 def show(self):
    print(self.__student_mark,self.__student_name)
class headmaster(teacher):
    pass

a1=teacher()
a1.mark()
a1.show()

class com():
 def __init__(self):
    self.__name="cgpt"
class show(com):
    print(__name)
b1=show()
b1()