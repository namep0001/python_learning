# BMI Calculator
print("Welcome to BMI Calculator")

height = float(input("What is your height?(M):"))
weight = float(input("What is your weight?(KG):"))
BMI = weight / (height * height)

if(BMI < 18.5):
    print(f"Underweight {BMI}")
elif(18.5 <= BMI <= 24.9):
    print(f"Healthy Weight {BMI}")
elif(25.0 <= BMI <= 29.9):
    print(f"Overweight {BMI}")
elif(BMI > 30.0):
    print(f"Obese {BMI}")