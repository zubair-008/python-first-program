
# thisDic= {"Name": "Zubair", "Age": 25, "Skill": "Python", "Name": "Zubair Tariq"}
# print("Name: ", thisDic["Name"])
# print("Age: ", thisDic["Age"])
# print("Skill: ", thisDic["Skill"])

employee = {
    "E-Code": 1000,
    "Name": "Zubair",
    "Age": 25,
    "Salary": 50000,
    "Skills": ["Python","Designing","Testing"]
    }

# print("E-Code: ", employee["E-Code"])
# print("Name: ", employee["Name"])
# print("Age: ", employee["Age"])
# print("Salary: ", employee["Salary"])
# print("Skills: ", employee["Skills"])

# print("Get All Keys: ", employee.keys())
# print("Get All Values Against Keys: ", employee.values())
# print("Get All Keys with Values: ", employee.items())


employee["Age"] = 30
employee["Location"]  = "Lahore"
employee["Last Name"] = "Tariq"
employee["Email"] = "zubairstarboy008@gmail.com"
employee["Cell No"] = "+923708922295"
print("Updated Dictionary is :", employee)

# print("All Keys in Dictionary: ", employee.keys())
# print("All Values in Dictionary: ", employee.values())
# print("All Items in Dictionary: ", employee.items())

employee.pop("Location")
# print("Employee after removing Location", employee)
employee["Skills"].append("Figma")
# print("Employee after Add item in Dictionary at the end: ", employee)
employee["Skills"].remove("Testing")
# print("Employee after removing Skill from Dictionary:", employee)
# x= employee.clear()
# print(x)
y=employee.copy()
print(y) 