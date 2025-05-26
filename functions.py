def add(num1, num2, operation):
    if operation == "+":
        total = num1 + num2  
    elif operation == "-":
          total = num1 - num2
    elif operation == "/":
      total = num1 / num2
    else:
        total = num1 * num2
    return total

num1 = float(input("Enter a number : "))
num2 = float(input("Enter a number : "))
operator = input("Enter the operator type (*,/,+,-) : ")

print(add(num1, num2, operator))

"""def my_function1(*kids):
  print("The youngest child is " + kids[4])

#my_function1("Emil", "Tobias", "Linus", "Sanctus")


def my_function1(**kids):
  print("The youngest child is " + child3 + ...)

#my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
"""

grade = int(input("Enter the score :"))

if grade >= 70:
    print("A")
elif grade >= 60:
    print("B")
elif grade >= 50:
    print("C")
elif grade >= 45:
    print("D")
elif grade >= 40:
    print("E")
elif grade <=39:
    print("F")
