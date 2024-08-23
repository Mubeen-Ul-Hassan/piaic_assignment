from random import randint

print("Welcome to the High-Low Game!")
print("-----------------------------")

round = 1
score = 0
while round != 6:
    user_guess = randint(0, 100)
    computer_guess = randint(0, 100)
    
    print(f"Round {round}")
    print(f"Your number is {user_guess}")
    lower_high = str(input("Do you think your number is higher or lower than the computers's?: ")).lower()

    if lower_high == 'higher' and user_guess > computer_guess:
            score += 1
            print(f"Your were right! The computer number was {computer_guess}.")
    elif lower_high == 'lower' and user_guess < computer_guess:
            score += 1
            print(f"Your were right! The computer number was {computer_guess}.")
    else:
        if (score != 0):
            score -= 1
        print(f"Aww, that's incorrect. The computer number was {computer_guess}")

    print(f"Your score is now {score} \n")

    round += 1
    if round == 6:
        print("Thanks for playing!")