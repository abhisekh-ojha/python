print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

#we have used if else and nested if else to make the game more interesting and user friendly
#we have used lower function to make the user input case insensitive
#we have used multiple if else to make the game more interesting and user friendly

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

question_1 = input("You're in the middle of Road - Where do you want to go first? Left or Right? ")

quest_1 = question_1.lower() #using lower function to lower the string

if quest_1 == "left": #asked user choice and moved to next question
  print("Nice choice, looks like you can win this game! Answer the second question.")
  river = input("You have came to near a river! Would you like to 'swim' or take a 'boat'?") #asked second question
  riv = river.lower()
  if riv == "swim": #given user boat option with consent
    print("Acha hai! Chal tujhe boat diya - Paani thanda hai")
    consent = input("chaiyee to haa kar warna na? 'haa' ya 'naa'") #taken consent as haa or Haa or else na and Naa
    if consent == "haa" or consent == "Haa":
      print("Okay now next and final question and you'll win or loose")
      quest_2 = input("Boat has came to end of the river, Select 'Win', 'Loose', or 'Skip' the option")
      ques_low = quest_2.lower()
      if ques_low == "win":
        print("wrong option, you loose")
      elif ques_low == "loose":
        print("hmm, you win! congrats")
      elif ques_low == "skip":
        print("okay my code work! you win")
      else:
        print("your output is wrong but still you win. Now mera mann nhi to code more haa")
    elif consent == "naa" or consent == "Naa":
      print("thik hai! game over - paani hi nhi hai")
    else:
      print("galat jawab! jaa you loose") #punished user if added his own word
  elif riv == "boat": #choosen boat in river ka question
    print("Aalsi! Boat me hole hai, Swim karega?")
    ask = input("Yes or No?") #asked yes no for swim. if selected yes then win or loose
    asked = ask.lower()
    if asked == "Yes" or asked == "No":
      print("jaa jeet gya man nhi mera aur code karne ka.")
    else:
      print("consent not match with Yes or No! you loose.")
elif question_1 == "right":
  print("Footi kismat! You loose") #choosen right so loose
else:
  print("Idiot! left or right pucha na! Jaa game over!") #punished user if added his own words
#game over