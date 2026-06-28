# BMI Calculator
print("Welcome to BMI Calculator")

height = float(input("What is your height?(M):"))
weight = float(input("What is your weight?(KG):"))
bmi = weight / (height * height)

if(bmi <= 18.5):
    print(f"Underweight {bmi}")
elif(18.5 <= bmi <= 24.9):
    print(f"Healthy Weight {bmi}")
elif(25.0 <= bmi <= 29.9):
    print(f"Overweight {bmi}")
else:
    print(f"Obese {bmi}")