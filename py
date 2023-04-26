# All of the functions, lists, modules etc are collected at the top for easy access.
import random
import time

money_variable = 1200
def pause():
  time.sleep(1)

def pause2():
  time.sleep(2)

#Asks user for a car, ignores their choice.
def illusionofchoice():
  while True:
    try:
          illusionofchoice_variable = int(input("Pick a car, from 1-6."))
    except ValueError:
          print("Please enter a valid integer")
          continue
    if illusionofchoice_variable >= 1 and illusionofchoice_variable <= 6:
          print(f'You want car number {illusionofchoice_variable}?')
          break
    else:
          print('The integer must be in the range 1-6')

def sadly():
  print("Sadly, the world doesn't work that way. Sometimes we can't have what we want.")

def colour():
  # Expanding on rand function
  mylist = ["yellow.","green.","a nice chrome.","purple???","a very specific shade of orange that cannot be described by any words known to mankind.","Ferrari Red®."]
  colour_variable = random.choice(mylist)
  print(str(carsentence)+", and it appears to be " + str(colour_variable))
  print()

# Information on bet.
def betinfo():
  print("Please place your bet.")
  pause2()
  print("You currently have $1200, from working a minimum wage job to feed your gambling addiction.")

def countdown():
  pause2()
  print("You have bet $"+str(bet_variable)+" on car #"+str(car_variable)+".")
  print()
  pause2()
  print("3")
  pause()
  print("2")
  pause()
  print("1")
  pause()
  print("Go!")

def announcement():
  print("The winner is car number...")
  pause()
  print(".")
  pause()
  print(".")
  pause()
  print(".")
  pause()
  print(str(winner_variable)+"!")

def profit():
  if winner_variable == car_variable:
    print("You have won $"+str(bet_variable*2)+".")
    print("You now have $"+str(money_variable+bet_variable)+".")
  else:
    print("You have lost $"+str(bet_variable)+". Did you know that 90% of gamblers quit right before their big win?")
#The actual game, using all the functions.
illusionofchoice()

sadly()

car_variable = random.randint(1,6)
print()
carsentence = "Your car is number "+str(car_variable)
colour()

pause2()
pause()

betinfo()

pause2()

while True:
     try:
         bet_variable = int(input("How much would you like to bet? "))
     except ValueError:
         print("Please enter a valid integer.")
         continue
     if bet_variable >= 1 and bet_variable <= 1200:
         print()
         break
     else:
         print('The integer must be in the range $1-$'+str(money_variable))

countdown()

winner_variable = random.randint(1,6)
if winner_variable == car_variable:
  winner_variable = random.randint(1,6)

pause()
print()

announcement()

pause()
profit()
