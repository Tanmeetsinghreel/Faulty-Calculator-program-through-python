
#Design a calculator which will corectly solve all the problems except the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4

#your programe should take operator and the two numbers as input from the user and then return the result.

print(" press 1 for addition\n"
      " press 2 for division\n press 3 for multiplication\n press 4 for subtraction\n and press enter key")
inpnum1 = int(input())

print("enter first number")
inpnum2 = int(input())

print("enter second number")
inpnum3 = int(input())

inpnum4 = inpnum2 + inpnum3
inpnum5 = inpnum2 / inpnum3
inpnum6 = inpnum2 * inpnum3
inpnum7 = inpnum2 - inpnum3

if inpnum2 == 56 and inpnum3 == 9:
    print("the addition of two numbers is 77",)
elif inpnum2 == 56 and inpnum3 == 6:
    print("the division of two numbers is 4")
elif inpnum2 == 45 and inpnum3 == 3:
    print("the multiplication of two numbers is 555")
elif int(inpnum1) == 1:
    print("the addition of two numbers is",inpnum4)
elif int(inpnum1) == 2:
    print("the division of two numbers is",inpnum5)
elif int(inpnum1) == 3:
    print("the multiplication of two numbers is",inpnum6)
elif int(inpnum1) == 4:
    print("the subtraction of two numbers is",inpnum7)
else:
    print("you have typed an invalid input")














