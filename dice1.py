import random
game_played=0
wins=0
while True:
    guess=input("Enter a number between 2 to 12 or enter q to quit game")
    if guess == "q":
        break
    try:
        guess = int(guess)
        if guess<2 or guess>12:
            print("Invalid guess, Guess again")
            continue

        roll_1=random.randint(1,6)
        roll_2=random.randint(1,6)
        roll = roll_1+roll_2
        if guess==roll:
            print("You win")
            wins+=1
        else:
            print("Sorry the dice value was",roll,"Try again")
        game_played+=1
    except ValueError:
        print("Invalied input, Enter again")

            

