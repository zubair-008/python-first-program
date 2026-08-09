age = int(input("Enter Your Age: "))
min_age =18
has_ID = False
can_Enter_Club = age >= min_age and has_ID
print("Can Enter In Club?", can_Enter_Club)
print(type(has_ID))