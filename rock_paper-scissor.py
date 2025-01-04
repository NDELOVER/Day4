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
import random
list_of_items = ["Rock", "Paper", "Scissors"]

play_again = True
while play_again:
    user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
    user_choice = list_of_items[user]
    print(user_choice)
    computer = random.choice(list_of_items)
    print(computer)
    if user_choice == "Rock" and computer == "Paper":
        print("You loose!")
    elif user_choice == "Rock" and computer == "Scissors":
        print("You won!")
    elif user_choice == "Paper" and computer == "Rock":
        print("You won!")
    elif user_choice == "Paper" and computer == "Scissors":
        print("You loose!")
    elif user_choice == "Scissors" and computer == "Rock":
        print("You loose!")
    elif user_choice == "Scissors" and computer == "Paper":
        print("You Won!")
    else:
        print("Tie!")
    check = input("Do you want to play again? Y or N ")
    if check == "N" or check == "n":
        play_again = False



