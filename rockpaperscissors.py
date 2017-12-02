import random

def rock_paper_scissors():
    result = 0
    result = result + random.randint(1,3)
    if result == 1:
        print("Your hand is Rock")
    elif result == 2:
        print("Your hand is Paper")
    else:
        print("Your hnad is Scissors")
rock_paper_scissors()
