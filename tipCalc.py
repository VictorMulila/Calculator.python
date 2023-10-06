
#Victor mulila
#sct211-0049/2022

def tip_calculator(bill_amount, tip_percentage, number_of_people):


  tip_amount = bill_amount * tip_percentage
  total_amount = bill_amount + tip_amount
  amount_per_person = total_amount / number_of_people
  return round(amount_per_person, 2)


bill_amount = float(input("Enter the bill amount: "))
tip_percentage_index = int(input("Choose a tip percentage (10%, 12%, or 15%): "))
tip_percentage = tip_percentage_index/100
number_of_people = int(input("Enter the number of people splitting the bill: "))


amount_per_person = tip_calculator(bill_amount, tip_percentage, number_of_people)

print(f"Each person should pay ${amount_per_person:.2f}.")
