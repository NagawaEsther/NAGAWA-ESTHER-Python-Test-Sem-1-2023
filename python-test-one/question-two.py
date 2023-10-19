# 2 i)
def calculate_average(x, y):
    return (x + y) / 2

# Testing the function with two different numbers
number1 = 2
number2 = 4

average = calculate_average(number1, number2)
print(f"The average of {number1} and {number2} is {average}")

#ii) 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Minimum number
minimum = min(num1, num2, num3)

# Outputing the minimum number
print(f"The minimum number is: {minimum}")