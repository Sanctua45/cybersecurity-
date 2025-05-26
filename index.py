"""#print("hello world")

def my_function1(*kids):
  print("The youngest child is " + kids[2])

#my_function1("Emil", "Tobias", "Linus")
  


def add(num1, num2, operation):
   if operation == "+":
      sum = num1 + num2
num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
print (num1 + num2)
"""

def myfunc():
  global x
  x = 300

myfunc()

print(x)