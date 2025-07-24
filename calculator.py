print("""__________________CALCULATOR_____________________
      PRESS 1 if you want to find addition of two numbers.
      PRESS 2 if you want to find subtraction of two numbers.
      PRESS 3 if you want to find multiplication of two numbers.
      PRESS 4 if you want to find division of two numbers.
      PRESS 5 if you want to find floor division of two numbers.
      PRESS 6 if you want to find modulus of two numbers.
      PRESS 7 if you want to find power of a number.
      """)
while True:
    operation=int(input("Enter the operation you want to perform --->"))
    first_number=int(input("Enter the first number-----> "))
    second_number=int(input("Enter the second number-----> "))
    if operation==1:
        result=first_number+second_number
        print("The addition of two number is : ",result)
    elif operation==2:
        result=first_number-second_number
        print("The subtraction of two number is : ",result)
    elif operation==3:
        result=first_number*second_number
        print("The multiplication of two number is : ",result)
    elif operation==4:
        result=first_number/second_number
        print("The division of two number is : ",result)
    elif operation==5:
        result=first_number//second_number
        print("The floor division of two number is : ",result)
    elif operation==6:
        result=first_number%second_number
        print("The modulus of two number is : ",result)
    elif operation==7:
        result=first_number**second_number
        print("The power of a number is : ",result)
    else:
        print("INVALID CHOICE")
    print("PRESS y if you want to continue\nPRESS n if you want to exit")
    ch=input("Do you want to continue----->")
    if ch=='n':
        print("Thanks!")
        break