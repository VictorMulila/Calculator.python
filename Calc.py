#Victor mulila
#sct211-0049/2022
class Calculator:
 def__innit__(self,x,y):
    self.x=x
     self.y=y
   
 def add(self,x, y):
  """Returns the sum of two numbers."""
   return x + y

 def subtract(self,x, y):
  """Returns the difference of two numbers."""
   return x - y

 def multiply(self,x, y):
  """Returns the product of two numbers."""
   return x * y

 def divide(self,x, y):
  """Returns the quotient of two numbers."""
   return x / y


print("Please select the operation you want to perform:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1, 2, 3, or 4): ")


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
calc=Calculator()

if choice == "1":
  result = calc.add(num1, num2)
elif choice == "2":
  result = calc.subtract(num1, num2)
elif choice == "3":
  result = calc.multiply(num1, num2)
elif choice == "4":
  result = calc.divide(num1, num2)
else:
  print("Invalid choice.")
  exit()


print("The result is:", result)
