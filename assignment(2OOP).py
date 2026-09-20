# Parent Class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child Class - Student
class Student(Person):

    def show_info(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)


# Child Class - Teacher
class Teacher(Person):

    def show_info(self):
        print("Teacher Name:", self.name)
        print("Teacher Age:", self.age)


# Objects
stu = Student("Ali", 20)
teacher = Teacher("Ahmed", 35)


# Polymorphism
stu.show_info()
teacher.show_info()
