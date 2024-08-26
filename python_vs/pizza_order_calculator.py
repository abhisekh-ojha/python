print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ") 
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

#using if else statements to calculate the price of the pizza.
#small pizza is $15, medium pizza is $20, large pizza is $25
#pepperoni for small pizza is $2, medium and large pizza is $3
#extra cheese for any size pizza is $1
# multiple if else statements are used to calculate the price of the pizza based on the size and the toppings.

price = 0
if size == "S":
  price += 15
  if add_pepperoni == "Y":
    price += 2
  if extra_cheese == "Y":
    price += 1
  print(f"Your final bill is: ${price}.")
elif size == "M":
  price += 20
  if add_pepperoni == "Y":
    price += 3
  if extra_cheese == "Y":
    price += 1
  print(f"Your final bill is: ${price}.")
elif size == "L":
  price += 25
  if add_pepperoni == "Y":
    price += 3    
  if extra_cheese == "Y":
    price += 1
  print(f"Your final bill is: ${price}.")
else:
  print("sorry we don't have that size available!")
