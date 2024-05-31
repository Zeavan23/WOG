# guess_game.py
import random

def generate_number(difficulty):
    return random.randint(0, difficulty)

def get_guess_from_user(difficulty):
    while True:
        guess = input(f"Guess a number between 0 and {difficulty}: ")
        if guess.isdigit() and 0 <= int(guess) <= difficulty:
            return int(guess)
        else:
            print("Invalid input. Please enter a number between 0 and", difficulty)

def compare_results(secret_number, user_guess):
    return secret_number == user_guess

def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    if compare_results(secret_number, user_guess):
        print("Congratulations! You guessed the correct number.")
        return True
    else:
        print(f"Sorry, the correct number was {secret_number}. You lost. Better luck next time.")
        return False

if __name__ == "__main__":
    print("Welcome to the Guess Game!")
    while True:
        difficulty = int(input("Enter the difficulty level (a positive integer): "))
        result = play(difficulty)
        if result:
            print("Congratulations! You won!")
        else:
            print("Do you want to play again? (yes/no): ")
            replay = input().lower()
            if replay != "yes":
                break
