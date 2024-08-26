#let's build a tip calculator which will split the bill within individuals

print("Welcome to the tip calculator!")
#used input function to get the user input and converted it to float and int.
bill = float(input("What is your total bill? $")) 
tip_in_percent = float(input("How much tip you like to give? 10, 12, or 15? %")) 
number_of_people = int(input("How many people to split the bill? "))

#calculating the tip and total bill
tip_in_dollar = bill * tip_in_percent / 100
total_bill = tip_in_dollar + bill
each_person_will_pay = total_bill / number_of_people

#formatted the final amount to 2 decimal places
final_amount = "{:.2f}".format(each_person_will_pay)

#used f-string to print the final amount
print(f"Each person should pay: ${final_amount}")
