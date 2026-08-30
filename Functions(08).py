# # Functions: A funtion is a block of code only runs when it is called.
# def Greet(name):
#     print(f"Hello {name}!")
# Greet("Zubair")


# def greek(name = "Ali"):
#     print(f"Hello {name}!")
# greek("Ahmed")

# def add_to_cart(item,quantity,price):
#     print(f"Added {quantity} {item} to the cart and the total Amount is {quantity*price}")

# add_to_cart("Apple", 2,20)
# add_to_cart("Banana", 6,60)

# # Class Activity
# # Write a program to take 5 students and welcome them to the class using functions

# def welcome(student):
#     print(f"Welcome to the Class {student}")
# welcome("Ali")
# welcome("Ahmed")
# welcome("Bilal")
# welcome("Zain")
# welcome("Ayesha")

# Bank Withdrawal Function

# def withdrawal(balance,amount):
#     if amount > balance:
#         print("Pehli Fursat mein Nikal hahahahah....")
#     else:
#         balance -= amount
#         print(f"Thory he reh gae hehehehe......: {balance}")
#     return balance
# withdrawal(10000,5000)

# Class Activity 2
# Question: Functions in Python

# Python mein ek function calculate_result() banayein jo 2 parameters name aur marks receive kare.

# Function ke andar:
# Student ke marks ki list ka sum calculate karein.
# Marks ki average calculate karein.
# Average ke basis par grade assign karein:
# 80 ya above → A
# 70–79 → B
# 60–69 → C
# 50–59 → D
# 50 se kam → F
# Student ka naam, total marks, average aur grade display karein.

# def calculate_result(name,marks):
#     total = sum(marks)
#     average = total / len(marks)
#     # print(f"Student name {name} and marks is {marks}")
#     if average >= 90:
#         Grade = "A"
#     elif average >= 80:
#         Grade = "B"
#     elif average >= 70:
#         Grade = "C"
#     else:
#         Grade ="F"
    
#     print("Student Name is:", name)
#     print("Total Marks is:", total)
#     print("Average is:", average)
#     print("Grade is:", Grade)


# calculate_result("Ali", [90,80,70,85])
# calculate_result("Bilal",[85,77,70,90])
# calculate_result("Raza",[90,90,90,90])
# calculate_result("Muzammil", [47,50,43,39])

# #Class Activity 3

# def sum(n1,n2):
#     return n1+n2
# print(sum(100,100))
# #Class Activity 4
# def calculate_Sum(num1,num2):
#     sum1 = num1+num2
#     print(sum1)
# calculate_Sum(100,50)


#Class Activity 4

def square_number(num1,num2,num3):
    return num1**num1,num2**num2,num3**num3
print(square_number(2))
print(square_number(4))
print(square_number(5))

def is_even(num):
    if num%2 == 0:
        print("Number is even")
    else:
        print("Number is Odd")
is_even(5)