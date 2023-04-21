print("Enter the operation to be performed:")
symbol=input('"+" for additon \n"-" for substaction \n"*"for multiplication\n "/" for division \n"%" to take modulus:  ')
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if symbol=="+":
    print("sum=",a+b)
elif symbol=="-":
    print("Difference=",a-b)
elif symbol=="*":
    print("Product=",a*b)
elif symbol=="/":
    if b!=0:
        print("Quotient=",a/b)
    else:
        print("Not defined")
elif symbol=="%":
    print("Reminder=",a%b)
else:
    print("Wrong input")