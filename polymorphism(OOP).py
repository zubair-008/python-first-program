#-----------------------------Polymorphism--------------------------

# class CreditCard():
#     def pay(self):
#         print("paying with Credit Card")

# class DebitCard():
#     def pay(self):
#         print("Paying with Debit Card")

# def process_payment(payment_method):
#     payment_method.pay()

# credit = CreditCard()
# debit = DebitCard()
# process_payment(credit)
# process_payment(debit)


#Class Activity

class Dog():
    def sound(self):
        print("Wofff")

class Cat():
    def sound(self):
        print("Meow")

dog = Dog()
dog.sound()
cat = Cat()
cat.sound()