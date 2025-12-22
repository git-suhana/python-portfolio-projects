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
print(rock)
games_images=[rock, paper, scissors]
import random
user_move= int(input("make your move-  type 0 for rock, 1 for paper and 2 for scissors"))
if(user_move>=0 and user_move<=2):
    print(games_images[user_move])
computer_move= random.randint(0,2)
print(computer_move)
print(games_images[computer_move])

if user_move>=3 or user_move<0:
    print("invalid! You lose")
elif user_move==0 and computer_move==2:
    print("you win")
elif(user_move<computer_move):
    print("you lose")
elif(computer_move==0 and user_move==2):
    print("you lose")
elif(user_move>computer_move):
    print("you wins")
elif(user_move==computer_move):
  print("sorry, its a draw")
