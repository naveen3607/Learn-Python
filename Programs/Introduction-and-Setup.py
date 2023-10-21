# Calculate the sum of the two numbers entered by the user
a = int(input("Enter the number 1 = "))
b = int(input("Enter the number 2 = "))
print("The sum of the two numbers entered by the user is", a + b)

# Convert temperature from Celsius to Fahrenheit
C = float(input("Enter the Celsius Temperature = "))
F = (32 + 9 / 5 * C)
print("The Fahrenheit Temperature = ", F)

# Write a Python program to calculate the area of a rectangle given its length and width
Length = float(input("Enter the Length of the rectangle = "))
Width = float(input("Enter the Width of the rectangle = "))
Area = Length * Width
print("The area of the rectangle is ", Area)

# Create a program that takes a user's name and age as input and prints a greeting message
Name = str(input("Enter your name = "))
Age = int(input("Enter your age = "))
print("Your name is", Name, end=" ")
print("Your age is", Age, end=" ")
print("Welcome to Python")

# Write a program to check if a number is even or odd
number = int(input("Enter the number = "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Given a list of numbers, find the maximum and minimum values
a = int(input("Enter the value = "))
b = int(input("Enter the value = "))
c = int(input("Enter the value = "))
d = int(input("Enter the value = "))
maximum = max(a, b, c, d)
print("The maximum number is", maximum)
minimum = min(a, b, c, d)
print("The minimum number is", minimum)

# Create a Python function to check if a given string is a palindrome
string = str(input("Enter the string = "))
reverse_string = string[::-1]
if string == reverse_string:
    print("The string is palindrome")
else:
    print("The string is not palindrome")

# Calculate the compound interest for a given principal amount, interest rate, and time period
principal_amount = float(input("Enter the principal amount = "))
interest_rate = float(input("Enter the interest rate = "))
time_period = float(input("Enter the time period = "))
compound_interest = principal_amount * ((1 + (interest_rate / 100)) ** time_period)
print("The compound interest is", compound_interest)

# Write a program that converts a given number of days into years, weeks, and days
days = int(input("Enter the number of days = "))
a = days // 365
b = days % 365
c = b // 7
d = b % 7
print("No. of years = ", a, end=" \n ")
print("No. of weeks = ", c, end=" \n ")
print("No. of days = ", d)


# Create a program that takes a sentence as input and counts the number of words in it
sentence = str(input("Enter the sentence = "))
print("The original string is:" + sentence)
res = sentence.count(" ") + 1
print("The number of word in the sentence is", res)

# Implement a program that swaps the values of two variables
a = int(input("Enter the value 1 = "))
b = int(input("Enter the value 2 = "))
a, b = b, a
print("The value of a after swapping: ", a)
print("The value of b after swapping: ", b)
