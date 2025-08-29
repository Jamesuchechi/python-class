number1 = float(input("input the first number"))
number2 = float(input("input the second number"))
operations = input("choose operations(+, -, *, /): ")

if operations == "+":
    result = number1 + number2
elif operations == "-":
    result = number1 - number2
elif operations == "*":
    result = number1 * number2
elif operations == "/":
    result = number1 / number2
else:
    result = "incorrect operations"

print("Result", result)
