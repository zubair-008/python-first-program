
name = "zubair tariq"
greetings = "Assalam-o-Alaikum!"
white_spaces = "      Zubair       Tariq         "
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(white_spaces.strip())

#concatination in String
name_with_greetings = greetings + " " + name
print(name_with_greetings)

#Reverse String Method

new_name = "madam"
reverse_name = new_name[::-1]
print(reverse_name)
if new_name == reverse_name:
    print(f"{new_name} is a palindrome.")
else:
    print(f"{new_name} is not a palindrome.")

# Replace String Charachter using replace string method

st1 = "Madam"
newst1 = st1.replace("a","A")
print(newst1)

# String count() Method
new_str = "HOW ARE YOU!"
new_str1 = new_str.count("A")
print(new_str1)

# String find() Method
txt = "Welcome to Pakistan"
new_txt = txt.find("Pakistan")
print(new_txt)

# Class Activity 1

fullName = input("Enter Your Full Name: ")
print(fullName.upper())
print(len(fullName))
if " " in fullName:
    print(f"{fullName} contain a space")
else:
    print(f"{fullName} not contain a space")


# Class Activity 2

messy_sentance = input("Enter Your Messy Sentance: ")
print(messy_sentance.strip())
print(messy_sentance.lower())
print(messy_sentance.count("a"))
print(messy_sentance.replace("a","A"))
print(messy_sentance.split())
print(len(messy_sentance))