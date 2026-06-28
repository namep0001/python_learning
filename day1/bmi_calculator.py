# BMI Calculator
print("Welcome to BMI Calculator")

height = float(input("What is your height?(M):"))
weight = float(input("What is your weight?(KG):"))
bmi = weight / (height * height)

if(bmi < 18.5):
    print(f"Underweight {bmi:.2f}")
elif(18.5 <= bmi <= 24.9):
    print(f"Healthy Weight {bmi:.2f}")
elif(25.0 <= bmi <= 29.9):
    print(f"Overweight {bmi:.2f}")
else:
    print(f"Obese {bmi:.2f}")