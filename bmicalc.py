#Victor mulila
#sct211-0049/2022

def calculate_bmi(weight, height):

  bmi = weight / (height ** 2)
  return bmi

def classify_bmi(bmi):

  if bmi < 18.5:
    return "Underweight"
  elif bmi >= 18.5 and bmi < 25:
    return "Normal"
  elif bmi >= 25 and bmi < 30:
    return "Overweight"
  else:
    return "Obese"

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)


bmi_category = classify_bmi(bmi)

print("Your BMI is:", bmi)
print("BMI category:", bmi_category)
