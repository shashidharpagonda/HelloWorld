"""Input two numbers and display the larger / smaller number."""

num1 = input("Enter integer number1:")
num2 = input("Enter integer number2:")
if int(float(num1)) > int(float(num2)):
    print(num1, ' is larger number')
    print(num2, ' is smaller number')
elif int(float(num1)) < int(float(num2)):
    print(num2, ' is larger number')
    print(num1, ' is smaller number')
else:
    print(num1," ", num2, ' are same')

