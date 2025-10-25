from abc import ABC,abstractmethod

class name(ABC):
 def student_nam(self):
    pass
class teacher():
  @abstractmethod
  def teacher_name(self):
    pass

class head_master(teacher):
 def teacher_name(self):
    print("sinthuja")

a1=head_master()
a1.teacher_name()
   