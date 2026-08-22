cart = ["Milk","Sugar","Bread","Rusk","Jam"]
cart.append("Drink") # Add item in list using append
print(cart) # Print Updated List
cart.insert(2,"Butter") # Add iten in list using Insert
print(cart) # Print Updated List
cart.remove("Rusk") # Remove Item form List
print(cart) # Print Updated List
cart[1]="Oil" # Update item in list by using indexing
print(cart)

# Print Items in list using For Loop
for i in cart:
    print ("Item in Cart: ", i)

print(len(cart))  # Print Length of The List  
