# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / (height * height)
if bmi < 18.5: #Under 18.5 they are underweight
  print(f"Your BMI is {bmi}, you have a under weight.")
elif bmi < 25: 
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30: #Equal to or over 25 but below 30 they are slightly overweight
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35: # Equal to or over 30 but below 35 they are obese
  print(f"Your BMI is {bmi}, you are obese.")
else: 
  print("Your BMI is {bmi}, you are clinically obese") #Equal to or over 35 they are clinically obese.