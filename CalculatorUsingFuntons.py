#Lecture-8 (23-08-2026)
#*Assignment:* "Simple Calculator Using Functions"

#Simple Calculator Using Function

def add(a,b):
    return a+b
print("Addition: ",add(5,10))

def subtract(a,b):
    return a-b
print("Subtract: ", subtract(50,15))

def multiply(a,b):
    return a*b
print("Multiply: ",multiply(5,5))

def divide(a,b):
    return a/b
print("Divide: ",divide(30,75))

def is_positive(num):
    if num >= 1:
        return True
    else:
        return False
print(is_positive(-7))