# Data Types, Numbers ,Operations, Type Conversion, f-Strings

# Tip_Calculator

print("\n----Billing Time----\n")
bill = float(input("What was the total bill?\n"))
tip = int(input("Tip - 10, 12, 15?\n"))
people_num = int(input("Number of people paying -\n"))

result = (bill+(bill*tip/100))/people_num

print("Each person should pay - " + str(result))