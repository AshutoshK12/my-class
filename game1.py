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
game_images = [rock ,paper,scissors]

user_choose = int(input("What do you choose ? type 0 for Rock , type 1 for Paper , type 2 for Sccisors...\n"))
print(game_images[user_choose])
computer_choice = random.randint(0 , 2)
print("computer choose:")
print(game_images[computer_choice])
if user_choose >= 3 or user_choose < 0:
    print("This is invalid number..")

elif user_choose == 0 and computer_choice == 2:
    print("you win..")

elif computer_choice == 0 and user_choose == 2:
    print("You lose..")

elif computer_choice > user_choose:
    print("You lose..")

elif computer_choice == user_choose:
    print(" it's Draw..")

elif user_choose > computer_choice:
    print("you win..")





