# variables / input
total_bill = float(input("Enter the total amount of bill:"))
people_number = int(input("How many people want to split the bill?:"))
tip_percentage = int(input("Tips percentage:"))

# compute
tip_amount = (tip_percentage * total_bill) / 100
grand_total = total_bill + tip_amount
fair_share = grand_total / people_number

# output
print (f"Tip Amount : {tip_amount:.2f} $ \n Total : {grand_total:.2f} $ \n Number of people : {people_number}\nEach person's share : {fair_share:.2f} $")