#Take temperature input from User
#Print "Hot" if value is greater than 35 and less than 40
#Print "Be Careful its too Hot!" if value is greater than 40
#Print "Warm" if value is greater than equal to 20 and less than equal to 35
#Print "Cold" if Condtion False
#Test the program by Changing Value of Temperature at least twice or re-running

temperature = int(input("Enter Temprature: "))
if(temperature >= 35 and temperature <= 40):
    print("Hot")
    if(temperature > 40):
        print("Be Careful its too Hot!")
elif(temperature >= 20 and temperature <= 35):
    print("Warm")
else:
    print("Cold")