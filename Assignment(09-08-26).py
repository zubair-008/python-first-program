# Store the prices of 3 menu items in variables

medium_Pizza = 1500
zinger_Burger = 450
biryani = 350

# calculate sub total by adding 3 items
sub_Total = medium_Pizza + zinger_Burger + biryani

# calculate services charges 10 percent
service_Charges = sub_Total * 10/100

# Add Flate 50Rs Delivery Fee
service_Charges +=50

# Calculate Final Bill AMount
total_Bill = sub_Total + service_Charges

# Print Total Payable Bill
print("YOur TOtal Payable Bill Is: ", total_Bill)

# Check Bill is greater than 1000
if(total_Bill >= 1000):
    print("True")
else:
    print("False")