#--------------------Inheritence(OOP)------------------------

# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print("Animal is speaking")


# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")
# dog = Dog("Buddy")


# class Cat(Animal):
#     def meow(self):
#         print("Cat is Meowing")
# cat = Cat("Whisker")

# dog.speak()
# dog.bark()
# cat.speak()
# cat.meow()


class Employee:
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
    def show_info(self):
        print(f"Name: {self.name}\nDesignation: {self.designation}\nSalary: {self.salary}\n")
class Developer(Employee):
    def coder(self):
        print("Developer is Coding")

class Manager(Employee):
    def manager(self):
        print("Manager is managing team")

dev = Developer("Zubair", 50000, "Developer")
dev.show_info()
dev.coder()

mgr = Manager("Ali", 60000, "Manager")
mgr.show_info()
mgr.manager()