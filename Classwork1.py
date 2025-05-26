class Parent:
  def __init__(self, add, subtract):
    self.multiply = add
    self.subtract = subtract

  def add(self):
    print(self.multiply, self.subtract)

s = Parent("Sanctus", "Nwaneri")
s.add()

class Child (Parent):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def add(self):
    print("Welcome", self.multiply, self.subtract, "to the class of", self.graduationyear)

s = Child("Mike", "Olsen", 2019)
s.add()