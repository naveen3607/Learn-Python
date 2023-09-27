#Career Guidance Project
a = str(input("Enter the field you want to join (App Developer, Web Developer, Data Science, Cyber Security) = "))
if (a == "App Developer"):
    b = str(input("Enter the field you want to join (Native, Hybrid) = "))
    if (b == "Native"):
        print("You can learn Java, Swift")
    else:
        print("You can learn Flutter, React Native")
elif (a == "Web Developer"):
    c = str(input("Enter the field you want to join (Frontend, Backend) = "))
    if (c == "Frontend"):
        print("You can learn HTML, CSS, JavaScript")
    else:
        print("You can learn Python, Java Script, Ruby, Java")
elif (a == "Data Science"):
    print("You can learn Python")
elif (a == "Cyber Security"):
    print("You can learn Networking")
else:
    print("Invalid")