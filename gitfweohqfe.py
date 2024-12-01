class Student:
    amout_of_students = 0
    print("HI")
    def __init__(self, height=160):
        self.height = height
        Student.amout_of_students+=1
    def grow(self, height=1):
      self.height+=height


sasha = Student()
masha = Student(height=170)

sasha.grow(height=15)

print(masha.height)
print(sasha.height)
print(Student.amout_of_students)