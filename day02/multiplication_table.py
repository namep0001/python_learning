# multiplication_table.py

number = int(input("Enter a number:"))
# if number is != int it gaves error/ program crash

for i in range (1, 10):
    print(f"{number} * {i} = " , number * i)

print("Do you want to enter another number? Y/N")
answer = str(input("Y for yes , N for no :"))
while(answer == "Y"):
    number = int(input("Enter a number:"))
    for i in range (1, 10):
        print(f"{number} * {i} = " , number * i)
    print("Do you want to enter another number? Y/N")
    answer = str(input("Y for yes , N for no :"))

if(answer == "N"):
    print("Closing the program ...")
elif (answer != "Y" or answer !="N"):
    print("Invalid Input.")
    print("Closing the program ...")
