import random
from replit import clear
from guess_the_number_art import logo, greeting, win, lose

def game(level):
  # Choose a random integer from 1 to 100
  number = random.randint(1, 100)

  # Select the dificulty level
  if level == 'easy':
    attempts = 10
  elif level == 'hard':
    attempts = 5
  else:
    print("Invalid input")

  # Start the game
  while attempts > 0:

    # Take the User Input
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    # Check the guess
    if guess == number:
      print(f"You got it! The answer was {number}.")
      print(win)
      break
    elif guess > number:
      print("Too high.")
      attempts -= 1
    elif guess < number:
      print("Too low.")
      attempts -= 1
    else:
      print("Invalid input. you lost a life")
      attempts -= 1

    # Check if the user has any attempts left
    if attempts == 0:
      print("You've run out of guesses, you lose.")
      print(f"The number was {number}.")
      print(lose)
      break


def main():
  # Print the logo and greeting
  print(logo)
  print(greeting)

  # Ask the user to choose the dificulty level
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

  # Start the game with the selected difficuilty level
  game(level)

  # Check if the user wants to play again
  play_more = input("Do you want to play more? Type 'y' or 'n': ").lower()

  # If the user wants to play again, clear the screen and start the game again
  if play_more == 'y':
    clear()
    main()
  else:
    print("Goodbye")


main()
