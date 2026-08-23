
class_directory = {}
class_directory["Ali"] = "Math"
class_directory["Bilal"] = "English"
class_directory["Ahmed"] = "Physics"
class_directory["Hamza"] = "Chemistry"
class_directory["Zafar"] = "Math"
# print(class_directory)

for name,subject in class_directory.items():
    print({name},{subject})
    x = class_directory.get(name)
    print(x)