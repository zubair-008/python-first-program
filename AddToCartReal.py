cart ={}

def add_cart(item,quantity,price):
    if item in cart:
        cart[item]["quantity"] += quantity
    else:
        cart[item] = {
            "quantity" : quantity,
            "price" : price
        }
    total = cart[item]["quantity"] * cart[item]["price"]
    print(f"Added {quantity} of {item} to the cart")
    print(f"price of the cart {item}:{total}")

# add_cart("Apple",2,200)


def remove_cart(item,quantity,price):
    if item in cart:
        removed = cart.pop(item)
        total = removed["quantity"] * removed["price"]

        print(f"{item} removed from the cart")
        print(f"Removed item total: {total}")
    else:
        print(f"{item} is not in the cart")

def show_cart(): 
    
    if not cart:
        print("Your Cart is Empty!")
        return
    print("\n----------Your Cart----------")
    grand_total = 0
    for item, details in cart.item():
        quantity = details["quantity"]
        price = details["price"]
        total = quantity * price

        print(f"{item} - Quantity: {quantity} - Price: {price} - Total: {total}")
        grand_total += total
    print("----------------")
    print(f"Grand Total: {grand_total}")

