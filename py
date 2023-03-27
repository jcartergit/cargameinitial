import random
import time


# The variable for this isn't necessary, it's left behind from when I tried to stop numbers over 6
illusionofchoice = int(input("Please pick a car, from numbers 1-6. "))
print()

print("Sadly, the world doesn't work that way. Sometimes we can't have what we want.")

# Playing around with delays
time.sleep(1)

# Random integers
car = random.randint(1,6)
carsentence = "Your car is number "+str(car)
print()

# Expanding on rand function
mylist = ["yellow.","green.","a nice chrome.","purple???","a very specific shade of orange that cannot be described by any words known to mankind.","Ferrari Red®."]
colour = random.choice(mylist)
print(str(carsentence)+", and it appears to be " + str(colour))
print()

# Delays are good, stops a flood of text.

time.sleep(3)
print("Please place your bet.")

time.sleep(2)
print("You currently have $1200, from working a minimum wage job to feed your gambling addiction.")

time.sleep(2)
bet = int(input("How much would you like to bet? "))

time.sleep(2)
print("You have bet $"+str(bet)+" on car #"+str(car)+".")
print()

time.sleep(2)
print("3")

time.sleep(1)
print("2")

time.sleep(1)
print("1")

time.sleep(1)
print("Go!")

winner = random.randint(1,6)

if winner == car:
  winner = random.randint(1,6)

time.sleep(1)
print()

print("The winner is car number...")

time.sleep(1)
print(".")

time.sleep(1)
print(".")

time.sleep(1)
print(".")

time.sleep(1)
print(str(winner)+"!")
