print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
step1= input('lets start...which side you want to go? type "left" or "right"')
step1=step1.lower()
if(step1== "left"):
    print("you are in the start of a lake, there is an island in middle of lake")
    step2= input('to cross the lake, type "wait" to wait for boat or "swim" to swim across for further move').lower()
    if(step2== "wait"):
        print("you have arrived at the island, there are 3 houses")
        step3= input("which door ?? type R to go to red house, B to blue house and Y to yellow house")
        if(step3== 'R'):
            print("Burned by fire!! Game over")
        elif(step3 == 'B'):
            print("Eaten by Beasts!! Game over")
        elif(step3== 'Y'):
            print("you win!!!")
        else:
            print("wrong command, Game over")
    else:
        print("Attacked by trout!! Game over")
else:
    print("fall into hole...Game over")