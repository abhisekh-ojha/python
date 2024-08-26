#using if else elif statement with multiple ifs

height = int(input("what is your height in cm? "))
bill = 0
if height >= 120: #checks if first condition is true
  print("you can ride the roller coaster")
  age = int(input("what is your age? "))
  if age < 12: #checks the age condition
    bill = 5
    print (f"Child ticket is ${bill}")
  elif age < 18:
    bill = 7
    print (f"Youth ticket is ${bill}")
  else:
    bill = 12
    print (f"Adult ticket is ${bill}")

  want_photos = input("Do you want the photo taken? Y or N? ") #added the variable to use multiple if's
  if want_photos == "Y": #using another if statement to add condition
    bill += 3 #this is shortcut to write bill = bill + 3

  print (f"Your final bill is ${bill}") #lastly printed the statement
else:
  print ("sorry you can't ride")