
class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

student_one = person("Zubair", 24, "Male")
student_two = person("Ali", 25, "Male")
student_three = person("Ahmed", 26, "Male")

print(f"\nName: {student_one.name} \nAge: {student_one.age} \nGender: {student_one.gender}")
print(f"\nName : {student_two.name} \nAge: {student_two.age} \nGender: {student_two.gender}")
print(f"\nName: {student_three.name} \nAge: {student_three.age} \nGender: {student_three.gender}")
