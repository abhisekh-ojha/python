# Which year do you want to check?
year = int(input("Please enter a year to check if it's a leap year: "))
# If the year is evenly divisible by 4, go to the next step. If not, it's not a leap year.
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year") 
  else:
    print("Leap year")
else:
  print("Not leap year")