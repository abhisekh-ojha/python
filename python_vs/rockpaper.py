rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors] #using list to store the value or diagram

print("Welcome to rock paper scissor game!")
user_choice = input("please select 0 for rock, 1 for paper and 2 for scissor\n")
user_choice = int(user_choice)

if user_choice >= 0 and user_choice <= 2:
  print("You Choose")
  print(game_images[user_choice])
else:
  print("Invalid Selection")

#used random module
import random
number = random.randint(0,2)

if user_choice >= 0 and user_choice <=2:
  if number == 0:
    print("Computer choose")
    print(rock)
  elif number == 1:
    print("Computer choose")
    print(paper)
  elif number == 2:
    print("Computer choose")
    print(scissors)
  else:
    print("It's tie, code didn't worked")

if user_choice >= 0 and user_choice <=2:
  if user_choice == number:
    print("It's Draw")
  elif user_choice == 0 and number == 1:
    print("You Loose")
  elif user_choice == 0 and number == 2:
    print("You Win")
  elif user_choice == 1 and number == 0:
    print("You Win")
  elif user_choice == 1 and number == 2:
    print("You Loose")
  elif user_choice == 2 and number == 0:
    print("You Loose")
  elif user_choice == 2 and number == 1:
    print("You Win")

else:
  print("Sorry no result due to invalid selection")