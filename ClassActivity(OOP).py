

class MobilePhone:
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)

    def apply_discount(self, discount):
        self.price = self.price - (self.price * discount / 100)


# Object banana
mobile1 = MobilePhone("Samsung", "Galaxy S24", 200000)

# Discount se pehle
print("Before Discount:")
mobile1.show_details()

# 10% discount apply karna
mobile1.apply_discount(10)

# Discount ke baad
print("\nAfter Discount:")
mobile1.show_details()
