
import random
# Define the game choices
CHOICES = ['rock', 'paper', 'scissors']

# Define a function to play the game
def play_game():
  # Ask the player to choose rock, paper, or scissors
  player = input("Choose rock, paper, or scissors: ").lower()

  # Check that the player's choice is valid
  if player not in CHOICES:
    print("Invalid choice. Please try again.")
    return

  # Choose a random option for the computer
  computer = CHOICES[random.randint(0, 2)]

  # Determine the winner
  if player == computer:
    print("It's a tie!")
  elif (player == 'rock' and computer == 'scissors') or \
       (player == 'paper' and computer == 'rock') or \
       (player == 'scissors' and computer == 'paper'):
    print("You win!")
  else:
    print("The computer wins!")

  # Print the computer's choice
  print(f"The computer chose {computer}.")

# Play the game
play_game()
