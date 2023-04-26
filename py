# All of the functions, lists, modules etc are collected at the top for easy access.
import random
import time

money = 1200
def pause():
  time.sleep(1)

def pause2():
  time.sleep(2)

#Asks user for a car, ignores their choice.
def illusionofchoice():
  while True:
    try:
          illusionofchoice = int(input("Pick a car, from 1-6."))
    except ValueError:
          print("Please enter a valid integer")
          continue
    if illusionofchoice >= 1 and illusionofchoice <= 6:
          print(f'You want car number {illusionofchoice}?')
          break
    else:
          print('The integer must be in the range 1-6')

def sadly():
  print("Sadly, the world doesn't work that way. Sometimes we can't      have what we want.")

def car():
  # Random integers
  car = random.randint(1,6)
  carsentence = "Your car is number "+str(car)
  print()

def colour():
  # Expanding on rand function
  mylist = ["yellow.","green.","a nice chrome.","purple???","a very   specific shade of orange that cannot be described by any words known to mankind.","Ferrari Red®."]
  colour = random.choice(mylist)
  print(str(carsentence)+", and it appears to be " + str(colour))
  print()

# Information on bet.
def betinfo():
  print("Please place your bet.")
  pause2()
  print("You currently have $1200, from working a minimum wage job to feed your gambling addiction.")

def bet():
  while True:
      try:
          bet = int(input("How much would you like to bet? "))
      except ValueError:
          print("Please enter a valid integer.")
          continue
      if bet >= 1 and bet <= 1200:
          print()
          break
      else:
          print('The integer must be in the range $1-$'+str(money))

def countdown():
  pause2()
  print("You have bet $"+str(bet)+" on car #"+str(car)+".")
  print()
  pause2()
  print("3")
  pause()
  print("2")
  pause()
  print("1")
  pause()
  print("Go!")

def winner():
  winner = random.randint(1,6)
  if winner == car:
    winner = random.randint(1,6)

def announcement():
  print("The winner is car number...")
  pause()
  print(".")
  pause()
  print(".")
  pause()
  print(".")
  pause()
  print(str(winner)+"!")

def profit():
  if winner == car:
    print("You have won $"+str(bet*2)+".")
    print("You now have $"+str(money+bet)+".")
  else:
    print("You have lost $"+str(bet)+". Did you know that 90% of gamblers quit right before their big win?")
#The actual game, using all the functions.
illusionofchoice()

sadly()

car()

colour()

pause2()
pause()

betinfo()

pause2()

bet()

countdown()

winner()

pause()
print()

announcement()

pause()
profit()
