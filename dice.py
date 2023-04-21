import random
wins = 0
rounds_played = 0

while True:
    guess = input("Enter the value of dice (2, 12) or type q to quit the game: ")
    if guess == "q":
        print("Thankyou for playing")
        break
    try:
        guess = int(guess)
        if guess < 2 or guess > 12:
            print("Invalid input value, please enter again.")
            continue
        
        roll_1 = random.randint(1, 6)
        roll_2 = random.randint(1, 6)
        roll = roll_1 + roll_2
        if guess == roll:
            print("Congratulations! You Win!")
            wins += 1
        else:
            print("Sorry, the total value of the dice is", roll)
        rounds_played += 1
    except ValueError:
        print("Invalid input value, please enter again.")

if rounds_played > 0:
    win_percent = (wins / rounds_played) * 100
    print("You played", rounds_played, "rounds, you won", wins, "times. Win percentage is", win_percent, "%")
