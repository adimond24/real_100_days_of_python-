from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("too low.")
        return turns - 1
    else:
        print(f"you got it! the answer was {actual_answer} ")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else: 
        return HARD_LEVEL_TURNS

def game():
    print("welcome to the number guessing game!")
    print("im thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    
    guess = 0
    while guess != answer: 
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        
game()