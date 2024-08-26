# Write your code here 👇

x = int(input("Enter the number between 1 to 100\n"))

if x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz")
elif x % 5 == 0:
    print("Buzz")
elif x % 3 == 0:
    print("Fizz")
else:
    print(f"number {x} doesn't seem to fizzbuzz")


#it's not a part of game. It's the way we can check fizz buzz in one between any 1 to 100

for number in range(1,101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 5 == 0:
    print("Buzz")
  elif number % 3 == 0:
    print("Fizz")
  else:
    print(number)
