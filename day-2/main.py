# Welcome the user to the program
print("Welcome to the tip calculator!")

# Ask for the total bill
total_bill = input("What was the total bill? ")
total_bill = float(total_bill[1:])

# Ask for the percentage of tip to give
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Ask for number of people who will pay in equal amounts
num_people = int(input("How many people to split the bill? "))

# Calculate the amount each person should pay
bill_per_person_no_tip = total_bill / num_people

tip_per_person = (tip_percentage / 100) + 1

bill_per_person_with_tip = bill_per_person_no_tip * tip_per_person

# Format the bill with tip per person to 2 decimal places
bill_per_person_with_tip = format(bill_per_person_with_tip, ".2f")

# Print how many people should pay
print("Each person should pay: $" + str(bill_per_person_with_tip))