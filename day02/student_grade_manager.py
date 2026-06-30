# student_grade_manager.py

print("Student Grade Manager Program Menu.")
print("please choose one option(1,2):\n 1- Add grade \n 2- Exit")
number_of_student = 0
total = 0
choice = 0
while( 1 > choice or choice > 2):
    choice = int(input("Your choice:"))

if( choice == 1):
    number_of_student = int(input("Please enter the number of students:"))
    for i in range (number_of_student):
        grade = float(input("Add grade:"))
        total = total + grade

    average = total / number_of_student
    print(f"Average: {average:.2f}")

else:
    print("Closing the program ...")
