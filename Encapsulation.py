# Example 1:             Encapsulation
# class Bank:
#     def __init__(self, pin, balance):
#         self.__pin = pin
#         self.__balance = balance

#     def deposit(self, pin, amount):
#         if pin != self.__pin:
#             print("Invalid Pin")
#             return
#         self.__balance += amount
#         print(f"Deposite {amount}. New Balance is: {self.__balance}")

#     def withdrawl(self, pin, amount):
#         if pin != self.__pin:
#             print("Invalid Pin")
#             return
#         if amount >= self.__balance:
#             print("Insufficient Balance")
#         else:
#             self.__balance -= amount
#             print(f"Withdrawal {amount}. New Balance is: {self.__balance}")
#     def get_balance(self,pin):
#         if pin != self.__pin:
#             print("Invalid Pin")
#             return
#         return self.__balance

# BankAccount = Bank("1234", 1000)
# BankAccount.deposit("1234", 500)
# BankAccount.withdrawl("1234", 200)
# print(BankAccount.get_balance("1234"))


# Example 2

class Parent:
    def __init__(self):
        self.__secret_key = "secret_key"   # __ Double underscore is for Private Variable
        self._protected_key = "protected_key" # _ single underscore is for protected
        self.public_key = "public_key" # without underscore is for public access

    def show_key(self):
        print("Secret Key:", self.__secret_key)

class Child(Parent):
    def __init__(self):
        super().__init__()

    def try_access(self):
        print("Trying to Access Key from child class:")
        # print("Secret Key: ", self.__secret_key)
        print("Protected Key: ", self._protected_key)
        print("Public Key: ", self.public_key)
        # self.show_key()

child = Child()
child.try_access()

