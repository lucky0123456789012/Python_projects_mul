score_Y = 0
score_N = 0
ask = input("do you want to play the game: ").lower()
if ask != "yes":
    print("the game is closed")
    quit()
print("Let's play the game")

answer1 = input("Is your computer with RAM more than 12GB: ").lower()

if answer1 == "yes":
    print("great")
    score_Y += 1
else:
    print("no")
    score_N += 1

answer2 = input("Is you computer having big screen: ").lower()

if answer2 == "yes":
    print("great")
    score_Y += 1
else:
    print("not possible to play on this screen")
    score_N += 1

answer3 = input("Is you computer having speakers: ").lower()

if answer3 == "yes":
    print("great")
    score_Y += 1
else:
    print("not possible to play with this speaker")
    score_N += 1


answer4 = input("are you having joystick: ").lower()

if answer4 == "yes":
    print("great")
    score_Y += 1
else:
    print("not possible to play without joystick")
    score_N += 1

print(f"As per the answer with YES the score :{score_Y} and with NO the score is {score_N}")