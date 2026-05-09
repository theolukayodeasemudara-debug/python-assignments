#  Ask user to input their weight in kilograms
#  Ask user for their height in meters
#  Calculate BMI using:
#       bmi = weight / (height * height)
#  Check BMI category:
#        18.5 = Underweight
#       18.5 - 24.9 = Normal
#       25 - 29.9 = Overweight
#       >= 30 = Obese
#  Print BMI and category

weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(meters): "))

bmi = weight / (height * height)

# print("BMI:", bmi)

if bmi < 18.5:
    print("Category: Underweight")
elif bmi <= 24.9:
    print("Category: Normal")
elif bmi <= 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")
