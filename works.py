
from re import I
from telnetlib import theNULL


num = int(input("enter any number:"))
factorial=1
if num < 0:
    print("sorry factorial is invalid")
elif num== 0:
    print ("The factorial of 0 is 1")
else:
    for i in range (1, num + 1):
        factorial = factorial * i
    print("factorial of ",num," is", factorial)