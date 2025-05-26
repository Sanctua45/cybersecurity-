operation=input("Enter the type of operation eg +,/,*,-")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

if operation=="+":
    print (num1 + num2)
elif operation=="/":
    print (num1 / num2)
elif operation=="*":
    print (num1 * num2)
else:
     print (num1 - num2)