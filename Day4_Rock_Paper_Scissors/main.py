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

images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(images[user_choice])

pc_choice = random.randint(0, 2)
print(f'Computer choice:\n{images[pc_choice]}')

if user_choice == pc_choice:
    print("It's a DRAW.")
elif user_choice == 0:
    if pc_choice == 2:
        print('You WON.')
    else:
        print('You LOST.')
elif user_choice == 1:
    if pc_choice == 0:
        print('You WON.')
    else:
        print('You LOST.')
elif user_choice == 2:
    if pc_choice == 1:
        print('You WON.')
    else:
        print('You LOST.')
