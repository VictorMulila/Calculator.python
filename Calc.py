def add(x, y):
  """Returns the sum of two numbers."""
  return x + y

def subtract(x, y):
  """Returns the difference of two numbers."""
  return x - y

def multiply(x, y):
  """Returns the product of two numbers."""
  return x * y

def divide(x, y):
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


if choice == "1":
  result = add(num1, num2)
elif choice == "2":
  result = subtract(num1, num2)
elif choice == "3":
  result = multiply(num1, num2)
elif choice == "4":
  result = divide(num1, num2)
else:
  print("Invalid choice.")
  exit()


print("The result is:", result)
