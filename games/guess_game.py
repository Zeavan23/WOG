import random

def generate_number(difficulty):
    return random.randint(0, difficulty)

def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f"Guess a number between 0 and {difficulty}: "))
            if 0 <= guess <= difficulty:
                return guess
            else:
                print("Invalid input. Please enter a number within the specified range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    return user_guess == secret_number

if __name__ == "__main__":
    print("Welcome to the Guess Game!")
    while True:
        difficulty = int(input("Enter the difficulty level (a positive integer): "))
        result = play(difficulty)
        if result:
            break

        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            break
