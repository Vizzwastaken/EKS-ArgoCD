# This is a simple calculator

print("------------------------")
print("       CALCULATOR ")
print("------------------------")


print("For Addition       press 1")
print("For Subtraction    press 2")
print("For Multiplication press 3")
print("For Division       press 4")

Operator = int(input("Select your Operation : "))

if Operator == 1:
    Num1 = int(input("Enter the First Number  : "))
    Num2 = int(input("Enter the Second Number : "))
    Res = Num1 + Num2
    print("The Result is = ", Res)
elif Operator == 2:
    Num1 = int(input("Enter the First Number  : "))
    Num2 = int(input("Enter the Second Number : "))
    Res = Num1 - Num2
    print("The Result is = ", Res)
elif Operator == 3:
    Num1 = int(input("Enter the First Number  : "))
    Num2 = int(input("Enter the Second Number : "))
    Res = Num1 * Num2
    print("The Result is = ", Res)
elif Operator == 4:
    Num1 = int(input("Enter the Numerator   : "))
    Num2 = int(input("Enter the Denominator : "))
    if Num1 == 0:
        print("Numerator cant be Zero")
    else:
        Res = Num1 / Num2
        print("The Result is = ", Res)
