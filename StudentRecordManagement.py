import random

students = []

def add_student():
    name = input("ENter Student Name: ").strip().title()
    has_number = any(char.isdigit() for char in name)
    if len(name)<3:
        print("Name must contains 3 letters")
        return
    elif has_number:
        print("Name Should Contain Only Letters")
        return
    course = input("ENter Course Name: " ).strip().title()
    english_marks = int(input("ENter Englsih Marks: "))
    math_marks = int(input("ENter Math Marks: "))
    science_marks = int(input("Enter Science Marks: "))
    student = {
        "name": name,
        "course": course,
        "marks": [english_marks, math_marks, science_marks]
    }
    students.append(student)
    print(students)

def view_record():
    if len(students) == 0:
        print("Not Found!")
    for student in students:
        print("Name:", student["name"])
        print("Course: ", student["course"])
        print("marks: ", student["marks"])

def search_Record():
    search_by_name = input("Enter Name for Search: ")

    for student in students:
        if student["name"] == search_by_name:
            print("Name: ", student["name"])
            print("Course: ",student["course"])
            print("Marks: ", student["marks"])
    else:
        print("Not FOund")

def update_marks():
    search_by_name = input("Enter Name for Search: ")
    for student in students:
        if student["name"] == search_by_name:
            print("Current Marks: ",student["marks"])
            english_marks = int(input("Enter New English Marks: "))
            math_marks = int(input("Enter New Math Marks: "))
            science_marks = int(input("Enter New Science Marks: "))

            student["marks"] = [english_marks,math_marks,science_marks]
            print(students)
            print("Marks Updated Successfully...")
        else:
            print("Student Not MFOund")


def class_statistic():
    total_marks = 0
    for student in students:
        total_marks = sum(student["marks"])
        print(total_marks)
        total_student = len(student)
        average = total_marks/ (total_student * 3)
        marks = student["marks"]
        if marks[0] >= 50 and marks[1] >=50 and marks[2] >= 50:
            print(student["name"]," - Pass")
        else:
            print(student["name"], " - Fail")

def random_student():
    student_of_the_day = random.choice(students) 
    print(student_of_the_day)

def delete_record():
    search_by_name = input("Enter Name You Want to Remove: ")
    for student in students:
        if student["name"] == search_by_name:
            students.remove(student)
            print(students)
    else:
        print("Student Not Found!")
choice = 0

while choice != 8:
    print("\n1. Add Student\n2. View Record\n3. Search\n4. Update Marks\n5. See Class Statics\n6. Student of Day\n7. Remove Students\n8. Exit")
    choice = int(input("Enter Your Choixe: "))
    if choice == 1:
        add_student()
        # print("Add Student")
    elif choice == 2:
        view_record()
        # print("View Records")
    elif choice == 3:
        search_Record()
        # print("Search")
    elif choice == 4:
        update_marks()
        # print("Update Marks")
    elif choice ==5:
        class_statistic()
        # print("Class Statics")
    elif choice == 6:
        random_student()
        # print("Student of The Day")
    elif choice == 7:
        delete_record()
        # print("Remove Students")
    elif choice == 8:
        print("Exit")
    else:
        print("Enter Valid CHoice")