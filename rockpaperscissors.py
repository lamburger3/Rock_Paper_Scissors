import random

def rock_paper_scissors():
    result1 = raw_input("Press Enter to play Rock-Paper-Scissors.")
    if result1 == result1:
        result = 0
    result = result + random.randint(1,3)
    if result == 1:
        print("Your hand is Rock")
    elif result == 2:
        print("Your hand is Paper")
    else:
        print("Your hand is Scissors")
    rock_paper_scissors()
rock_paper_scissors()

