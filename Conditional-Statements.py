#Conditional statements
age = int(input("Enter your age = "))
if age>18:
    print("You are adult")
else:
    print("You are child")

#Maximum of 2 numbers
a = int(input("Enter the number 1 = "))
b = int(input("Enter the number 2 = "))
if a>b:
    print("The maximum number is", a)
elif b>a:
    print("The maximum number is", b)
else:
    print("Both are equal")

#Logical Operators
physics = int(input("Enter physics marks = "))
chemistry = int(input("Enter chemistry marks = "))
if (physics>35) and (chemistry>35):
    print("Pass")
elif (physics>35) and (chemistry < 35):
    print("Physics is passed and Chemistry is failed")
elif (physics <35) and (chemistry>35):
    print("Chemistry is passed and Physics is failed")
else:
    print("Fail")

age = int(input("Enter the age = "))
if age>=18:
    print("The person is adult")
elif 13<= age <= 17:
    print("The person is teenager")
else:
    print("The person is child")

#Nested IF-ELSE
a = int(input("Enter your age = "))
if (a >= 14):
    if (a>=18):
        print("You are Adult")
    else:
        print("You are Teenager")
elif (a>=1) and (a<=13):
    print("You are child")
else:
    print("Invalid")

