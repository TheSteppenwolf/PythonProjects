#Write your code below this line 👇
import game_module
import random

# Computer choice
computer_option = str(random.randint(0,2))

# Player choice
user_option = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\nChoice: ")

# Printing of the results
print(f"Your choice: {game_module.get_name(user_option).capitalize()}")
print(game_module.choose(user_option))
print(f"Computer choice: {game_module.get_name(computer_option).capitalize()}")
print(game_module.choose(computer_option))

# Printing the winner, loser or tie
if game_module.get_winner(user_option, computer_option) == 0:
    print("Congratulations! You Won!")
elif game_module.get_winner(user_option, computer_option) == 1:
    print("Bad Luck! You Lost!")
else:
    print("It's a Tie!")
