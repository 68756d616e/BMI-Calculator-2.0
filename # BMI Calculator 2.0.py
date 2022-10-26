# BMI Calculator 2.0
# An updated version of the original BMI calculator

# You input a Height and Weight in KG and M
height = float(input("Please input your height in M: "))
weight = float(input("Please input your weight in kg: "))

# The BMI total is the Weight divided by the Height squared
bmi_total = weight / height ** 2

# Below we round the total number of the BMI

if round(bmi_total) <= 18:
  print(f"Your BMI is {round(bmi_total)}, you are underweight.")
elif round(bmi_total) <= 22:
  print(f"Your BMI is {round(bmi_total)}, you have a normal weight.")
elif round(bmi_total) <= 28:
  print(f"Your BMI is {round(bmi_total)}, you are slightly overweight.")
elif round(bmi_total) <= 33:
  print(f"Your BMI is {round(bmi_total)}, you are obese.")
elif round(bmi_total) == 40:
  print(f"Your BMI is {round(bmi_total)}, you are clinically obese.")
else:
  print("Meh, you have hard work ahead")