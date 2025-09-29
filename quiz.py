score = 0
ask = input("do you want to play the game: ").lower()
if ask != "yes":
    print("the game is closed")
    quit()
print("Let's play the game")

answer1 = input("Is your computer with RAM more than 12GB: ").lower()

if answer1 == "yes":
    print("great")
    score += 1
else:
    print("incorrect")

answer2 = input("Is you computer having big screen: ").lower()

if answer2 == "yes":
    print("great")
    score +=1
else:
    print("not possible to play on this screen")

answer3 = input("Is you computer having speakers: ").lower()

if answer3 == "yes":
    print("great")
    score +=1
else:
    print("not possible to play with this speaker")


answer4 = input("are you having joystick: ").lower()

if answer4 == "yes":
    print("great")
    score +=1
else:
    print("not possible to play on this screen")

print(f"As per the anser with YES the score {score}")