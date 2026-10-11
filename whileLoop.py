correct_pin = 1234
enterd_pin = ""

while enterd_pin != correct_pin:
    enterd_pin = int(input("Enter Your Pin:"))
    print(type(enterd_pin))
    if enterd_pin != correct_pin:
        print("Incorrect Pin. Please Try Again.")
print("Correct Pin. Access Successfully")
