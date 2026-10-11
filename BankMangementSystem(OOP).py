
class AccountOpeningDetails:
    def __init__(self,name,f_name,cnic,email,account_type,balance):
        self.name = name
        # self.f_name = f_name
        # self.cnic = cnic
        # self.email = email
        # self.account_type = account_type
        self.balance = balance
    def deposit_amount(self,amount):
        self.balance += amount
        print(f"Your Deposited Amount is: {amount}")
    def withdrawal(self,amount):
        if amount > self.balance:
            print("Insuficient Balance")
        else:
            self.balance -= amount
            print(f"Withdrawal Successfully...{amount}")
            print(f"Your Remaining Balance is: {self.balance}")
BankAccountOpner = AccountOpeningDetails("Zubair","Tariq","12345-6789012-3","zubair@gmail.com","Saving", 0)
# print(BankAccountOpner.name)
BankAccountOpner.deposit_amount(20000)
BankAccountOpner.withdrawal(10000)