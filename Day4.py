# About psudorandom number generation and setting seeds: 
# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
# https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators
 
#1: Random numbers: 
import random as rd
random_float= rd.random()
print(random_float)
random_int = rd.randint(1,100)
print(random_int)

#2: Heads or Tails:
import random 
random_side = random.randint(0,1)
if random_side ==1:
  print("Heads")
else:
  print("Tails")

# On data structures: https://docs.python.org/3/tutorial/datastructures.html
  
#3: Banker Roullete:
import random
# Split string method
# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
names_string = input("Give me everybody's names, separated by a comma. ")
# split is a devider function 
names = names_string.split(", ")
#Get the total number of items in list.
num_items = len(names)
#Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today!")

# OR: 
import random
names_string = input("Give me everybody's names, separated by a comma. ")
# split is a devider function 
names = names_string.split(", ")
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today!")

#4: 





# Rock/Paper/Scissors Program: 

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!") 
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
