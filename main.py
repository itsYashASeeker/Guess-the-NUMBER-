import random
from label import labels
print(labels)
print("I am thinking a number between 1 and 100")
difficulty=input("What Difficulty do you want to choose? 'Hard' or 'Easy'? ").lower()
number=random.randint(1,100)


def glass():
  for i in range(1, attempts+1):
    ask=int(input(f"Attempt no. {i}:\nGuess a Number!! "))
    if ask>number:
      print("***************\nToo High!\n***************")
    elif ask<number:
      print("***************\nToo Low\n***************")
    elif ask==number:
      print("***************\nYou Guessed it Right!! You Won!")
      break
    else:
      print("Please Enter a Valid Integer")
      i -= 1 
  if not ask==number:
    print("You Run out of guesses!! You lose!")
    print(f"The correct answer is {number}")

if difficulty=="hard":
  attempts=5
  print("You have 5 Attempts!")
  glass()
elif difficulty=="easy":
  attempts=10
  print("You have 10 Attempts!")
  glass()
else:
  print("Please Enter Valid Input!") 

     
