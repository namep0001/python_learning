# guess_the_number.py

number_to_guess = 20
number_of_tries = 1

print("Guess the number challenge\n It's a number between 1 to 100")
guessed_num = int(input("Your guess?:"))

if(number_to_guess == guessed_num):
    print(f"You guessed right! {number_to_guess} was the correct number, you tried {number_of_tries} times.")

while(number_to_guess != guessed_num):
    if(guessed_num < number_to_guess):
        print("Higher!")
        number_of_tries = number_of_tries + 1
    elif(guessed_num > number_to_guess):
        print("Lower!")
        number_of_tries = number_of_tries + 1
    guessed_num = int(input("Your guess?:"))
    if(number_to_guess == guessed_num):
        print(f"You guessed right! {number_to_guess} was the correct number, you tried {number_of_tries} times.")
