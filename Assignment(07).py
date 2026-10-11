product = {
    "Name": "Shirt",
    "Price": 2000,
    "Quantity": 2,
}

print("Name: ",product["Name"],
"Price: ", product["Price"], 
"Quantity: ", product["Quantity"])

product["Price"] = 2500
print(product)

product["Category"] = "Clothing"
print(product)

if "discount" in product:
    print("Discount exist")
else:
    print("Discount not available")

newProduct = {
    "Name": "Trouser",
    "Price": 3000,
    "Quantity": 1
}
shareInfo = {
    "Store": "Fashin.pk"
}
product.update(shareInfo)
newProduct.update(shareInfo)
print("Update ho gai product Dictionary : ",product)
print("Update ho gai New Product Dictionary: ", newProduct)