#Victor mulila
#sct211-0049/2022

import datetime

"""def age_calculator(year_of_birth):
  

  today = datetime.date.today()
  birth_date = datetime.date(year_of_birth, 1, 1)
  age = today - birth_date

  years = age.days // 365
  months = (age.days % 365) // 30
  days = (age.days % 365) % 30

  return years, months, days



year_of_birth = int(input("Enter your year of birth"))
years, months, days = age_calculator(year_of_birth)

print(f"Age: {years} years, {months} months, and {days} days.")"""


import datetime

def age_calculator(date_of_birth):

  
  date_of_birth_list = date_of_birth.split("/")
  day = int(date_of_birth_list[0])
  month = int(date_of_birth_list[1])
  year = int(date_of_birth_list[2])

  
  today = datetime.date.today()
  birth_date = datetime.date(year, month, day)
  age = today - birth_date

  years = age.days // 365
  months = (age.days % 365) // 30
  days = (age.days % 365) % 30

  return years, months, days

# Example usage:

date_of_birth =  input("Enter your date of birth in the format DD/MM/YY :")
years, months, days = age_calculator(date_of_birth)

print(f"Age: {years} years, {months} months, and {days} days.")


