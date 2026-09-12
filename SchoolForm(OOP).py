class SchoolForm:
    def __init__(self, f_name, l_name, age, gender, email, address, p_number, total_fee):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender
        self.email = email
        self.address = address
        self.p_number = p_number
        self.total_fee = total_fee
        self.fee = 0

    def deposit(self, fee_amount):
        if fee_amount <= 0:
            print("Invalid Amount")
        elif fee_amount > self.total_fee - self.fee:
            print("Amount is greater than pending fee")
        else:
            self.fee += fee_amount
            pending = self.total_fee - self.fee

            print(f"Fee Deposit Amount is: {fee_amount}")
            print(f"Total Paid Fee is: {self.fee}")
            print(f"Pending Fee Amount is: {pending}")


admission_form = SchoolForm(
    "Zubair", "Tariq", 25, "Male",
    "zubair@gmail.com", "Lahore",
    "123456789012", 10000
)

admission_form.deposit(3000)
