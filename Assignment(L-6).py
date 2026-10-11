# Individually, in VS Code, each student writes a program that:
# 1. Creates a list of 5 numbers of their choice.
# 2. Prints the first, last, and third item using indexing.
# 3. Updates one value in the list.
# 4. Removes one item from the list.
# 5. Prints the final list, along with its len() , max() , and min().

list = [100,200,300,400,500]
print(list[0],list[-1],list[2]) # Prints the first, lasr and third item using index
list.append(600) # Update one value in the list
print("Update Item From List :",list) # Prints updated List
list.remove(200) #Remove one Item From List
print("Remove Item From List: ",list) # Print List After Remove One Item
print("Maximum Number From List: ",max(list)) # Print Maximum Number From List
print("Minimum Number From List: ",min(list)) # Print Minimum Number From List
print("Total Length of List: ",len(list)) # Print Length of List