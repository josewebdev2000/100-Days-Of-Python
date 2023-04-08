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

options = [rock, paper, scissors]

# Let the user choose
human_choice = input("rock, paper, or scissors (R/P/S)? ")

# Process the human choice
if human_choice.lower() == "r":
    human_choice = rock

elif human_choice.lower() == "p":
    human_choice = paper

elif human_choice.lower() == "s":
    human_choice = scissors

else:
    print("Invalid choice\nThe option rock will be assigned automatically to you")
    human_choice = rock

# Pick a random choice for the computer
computer_choice = random.choice(options)

# Print each choice
print("Your choice")
print(human_choice)
print("\nComputer's choice")
print(computer_choice + "\n")

# Compare
if (human_choice == rock and computer_choice == scissors) or (human_choice == scissors and computer_choice == paper) or (human_choice == paper and computer_choice == rock):
    print("You win!")

elif (human_choice == rock and computer_choice == paper) or (human_choice == scissors and computer_choice == rock) or (human_choice == paper and computer_choice == scissors):
    print("You lose")

else:
    print("Tie")
