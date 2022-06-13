# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
# https://docs.python.org/3/library/functions.html

#1: Most simmple function ever:
def my_function():
  print("Hello")
  print("Bye")
my_function()

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
#2: Drawing a square:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
# Draw a square 
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
#3: Hurdle Loop Challenge: 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for step in range(6):
    jump()

# https://peps.python.org/pep-0008/
# Indentention in Python and style of code is critically important! 

#4: 













