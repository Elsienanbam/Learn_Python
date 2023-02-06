def currency_converter():
    print("choose one of the following:")
    print("1. Convert Naira to dollar")
    print("2. Convert Naira to pounds")
    print("1. Convert Naira to euro")
    choice = int(input("what would you like to do?"))
    naira = int(input("How much naira do you want to convert? "))
    if choice == 1:
        sum = naira * 430
        print(naira, "is equivalent to ", sum, " dollars")
    elif choice == 2:
        sum = naira * 500
        print(naira, "is equivalent to ", sum, "pounds")
    elif choice == 3:
        sum = naira * 500
        print(naira, "is equivalent to ", sum, "euro")
    else:
        print("invalid response, please try again")

print("=====Welcome to the value converter====")
print("Please select one of the options below to proceed:")
print("1. Currency converter")
print("2. Temperature converter")
print("3. Length converter")
choice = int(input("Enter your choice: "))
if choice == 1:
    currency_converter()
else:
    print("Sorry, this function is not available yet.")

    # find out about typecasting and exceptions
