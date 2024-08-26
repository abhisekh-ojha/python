#band name generator, in this project we will create a simple band name generator program
print("Hello! Welcome to Band Name Generator Program")
print ("We're going to ask you few question, before we suggest you a name")
#greeted the customers first with print statement
confirm = input("Ready (yes/no)\n") #used input function to ask yes and no
#using if and else function to show desired result
if confirm == "yes":
    print("okay, let's start")
    name = input("what is your first name?\n")
    pet = input("what is your pet name\n?")
    print(pet + " " + name + " band wala")
else:
    print("okay, not a problem! see you next time")