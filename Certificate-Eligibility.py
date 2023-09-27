#Certificate Eligibility
a = str(input("Are you part of CWS? (yes or no) = ")).lower()
if (a == "yes"):
    b = int(input("Enter the number of classes attended = "))
    if(b>=3):
        c = int(input("Enter the number of assignments submitted = "))
        if (c>=3):
            print("You are eligible for certificate")
        else:
            print("You are not eligible for certificate because you did not submit enough assignments")
    else:
        print("You are not eligible for certificate because you attended less than 3 classes")
else:
    print("Sorry, you are not eligible for certificate")