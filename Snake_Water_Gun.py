import random

# '''1 for Snake
# -1 for Water 
# 0 for Gun
# '''

# Computer makes a random choice
computer = random.choice([1, -1, 0])

you = input('Enter your Choice (s for Snake, w for Water, g for Gun): ').lower()
you_dict = {"s": 1, "w": -1, "g": 0}

if you not in you_dict:
    print("Invalid choice! Please enter s, w, or g.")
else:
    younum = you_dict[you]

    print(f"Computer chose: {computer}")

    if (computer == -1 and younum == 1):
        print("You Win!!")

    elif (computer == -1 and younum == 0):
        print("You Lose!!")

    elif (computer == 1 and younum == -1):
        print("You Lose!!")

    elif (computer == 1 and younum == 0):
        print("You Win!!")

    elif (computer == 0 and younum == -1):
        print("You Win!!")

    elif (computer == 0 and younum == 1):
        print("You Lose!!")

    elif (computer == younum):
        print("It's a Draw!!")

    else:
        print("Something Went Wrong")
