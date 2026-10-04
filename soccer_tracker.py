# def clear() is what will be used to create a clear screen after inputs
def clear():
   print("\n" * 100)
def space():
   print("\n" * 4)
#This is where the introduction is stated
print("Welcome to the Soccer Tracker!")
#Asks for the user's name
name = input("What is your name?")
clear()
#Asks for the user's age
age = input("How old are you?")
clear()
#Asks for user's position
print("Select your position:")
print("1. LW/RW")
print("2. CAM")
print("3. CDM")
print("4. CM")
print("5. LM/RM")
print("6. CB")
print("7. LB/RB")
position = input("Your Position: ")
clear()
#Asking for the user's dominant foot
foot = input("What's your dominant foot?: ")
clear()
#Asks for a rating of the user's skills
print("Now, rate yourself out of 10 on the following skills:")
dribbling = input("1. Dribbling:")
shooting = input("2. Shooting/Finishing:")
passing = input("3. Passing:")
stamina = input("4. Stamina:")
speed = input("5. Speed:")
defending = input("6. Defending:")
iq = input("7. Soccer IQ:")
clear()
space()
#The Final Results/Profile
print("YOUR PROFILE")
print(f"NAME: {name.upper()}")
print(f"AGE: {age}")
print(f"POSITION: {position.upper()}")
print(f"DOMINANT FOOT: {foot.upper()}")
print("SKILLS")
print(f"1.DRIBBLING: {dribbling}")
print(f"2.SHOOTING/FINISHING: {shooting}")
print(f"3.PASSING: {passing}")
print(f"4.STAMINA: {stamina}")
print(f"5.SPEED: {stamina}")
print(f"6.DEFENDING: {defending}")
print(f"7.SOCCER IQ: {iq}")





