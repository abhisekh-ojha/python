#we will create head and tail game using python
import random

print("Welcome to the Head or Tail Game!")
rem = random.randint(0,1)
if rem == 0:
  print("It's Heads")
else:
    print("It's Tails")