print("The Love Calculator is calculating your score...")
name1 = input("what is your full name? ")
name2 = input("what is your partner full name? ") 

#.lower() method is used to convert the string to lowercase
s_name1 = name1.lower()
s_name2 = name2.lower()

full_name = (s_name1 + " " + s_name2) #concatenating the two strings

#.count() method is used to count the number of times a specific value appears in the string
t = full_name.count("t")
r = full_name.count("r")
u = full_name.count("u")
e = full_name.count("e")

l = full_name.count("l")
o = full_name.count("o")
v = full_name.count("v")
e = full_name.count("e")

#converting the count to string to concatenate
total_true = str(t+r+u+e)
total_love = str(l+o+v+e)
love_percent = (total_true + total_love)

#converting the string to integer
love_percent = int(love_percent)

#using if else elif statement to show the result
#using logical operators to check the condition

if love_percent <= 10 or love_percent > 90:
  print(f"Your score is {love_percent}, you go together like coke and mentos.")
elif love_percent >= 40 and love_percent <= 50:
  print(f"Your score is {love_percent}, you are alright together.")
else:
  print(f"Your score is {love_percent}.")
#done