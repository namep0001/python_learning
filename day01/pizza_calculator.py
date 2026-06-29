# Pizaa Calculator

total_slices = 0
people_number = 0

# User Input For XX People
people_number = int(input("How many people attending party?"))
while(people_number <= 0):
    print("Invalid Input!")
    people_number = int(input("How many people attending party?"))

for i in range(people_number):
    slices = int(input("Enter the amount of slice(s):"))
    while (slices <=0):
        print("Invalid input!")
        slices = int(input("Please re-enter the amount of slice(s)!:"))
    
    total_slices = total_slices + slices

# Other Informaion
average_pizza_slice = int(input("What is the average pizza slice in your country? (In Amrican average is 8 slice) = Answer:"))
pizza_price = float(input("Enter the pizza price:"))

# Compute / Process
whole_pizza = total_slices // average_pizza_slice
remainder_slice = total_slices % average_pizza_slice
if(remainder_slice > 0):
    whole_pizza = whole_pizza +1

# Output
if(remainder_slice == 0):
    print("Perfect!")
else:
    print("Your slices do not match with the required pizza.")
    
print("You need to buy" , whole_pizza , "pizza(s)!")
print("The price you need to pay is : ", pizza_price * whole_pizza ,"$")
