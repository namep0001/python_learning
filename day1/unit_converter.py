# Unit Converter
# km → miles $$ 1 kilometer = 0.6213711922 mile / 1 Mile = 1.609344 Kilometer
# kg → lbs $$ 1 kilogram = 2.2046226218 pound / 1 Pound = 0.453592 Kilogram
# centimetre → inch $$ 1 centimeter = 0.3937007874 inch / 1 Inch = 2.54 Centimeter

print("Welcome to Unit Convertor")
print(
"Type 1 to convert km to mile.\n Type 2 to convert miles to km.\n Type 3 to convert kg to lbs.\n Type 4 to convert lbs to kg.\n Type 5 to convert centimetre to inch.\n Type 6 to convert inch to centimetre.")
choice = int(input("Your choice:"))
number_to_convert = float(input("Enter the number you want to convert:"))
if(choice == 1):
    print("1- km to mile.")
    miles_conv = number_to_convert * 0.6213711922
    print(f"{number_to_convert} km is {miles_conv:.2f} mile.")
elif(choice == 2):
    print("2- miles to km.")
    km_conv = number_to_convert * 1.609344
    print(f"{number_to_convert} mile is {km_conv:.2f} km.")
elif(choice == 3):
    print("3- kg to lbs.")
    lbs_conv = number_to_convert * 2.2046226218
    print(f"{number_to_convert} kg is {lbs_conv:.2f} pound/lbs.")
elif(choice == 4):
    print("4- lbs to kg.")
    kg_conv = number_to_convert * 0.453592
    print(f"{number_to_convert} pound/lbs is {kg_conv:.2f} kg.")
elif(choice == 5):
    print("5- centimetre to inch.")
    inch_conv = number_to_convert * 0.3937007874
    print(f"{number_to_convert} centimetre is {inch_conv:.2f} inch.")
elif(choice == 6):
    print("6- inch to centimetre.")
    centimetre_conv = number_to_convert * 2.54
    print(f"{number_to_convert} inch is {centimetre_conv:.2f} centimetre.")
else:
    print("Invalid choice.")