from utils import add_score, get_player_score
from games.memory_game import play_memory_game
from games.guess_game import play as play_guess_game
from games.currency_roulette_game import play as play_currency_roulette_game
import os

def clear_console():
    if os.name == 'nt':  # Pour Windows
        _ = os.system('cls')
    else:  # Pour Mac et Linux
        _ = os.system('clear')

def welcome(username):
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")

def start_play(username, api_key):
    # Supprimer l'affichage du score ici
    while True:
        print("Please choose a game to play:")
        print("1. Memory Game - a sequence of numbers will appear for 3 seconds and you have to guess it back.")
        print("2. Guess Game - guess a number and see if you chose like the computer.")
        print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

        game_choice = input("Enter the number corresponding to the game you want to play: ")

        if game_choice not in ['1', '2', '3']:
            print("Invalid choice. Please enter a number between 1 and 3.")
            continue

        difficulty = input("Enter the difficulty level (1-5): ")

        if difficulty not in ['1', '2', '3', '4', '5']:
            print("Invalid difficulty level. Please enter a number between 1 and 5.")
            continue

        difficulty = int(difficulty)

        if game_choice == '1':
            clear_console()  # Clear the screen before starting the game
            print(f"Starting Memory Game with difficulty level {difficulty}")
            result = play_memory_game(difficulty)
        elif game_choice == '2':
            print(f"Starting Guess Game with difficulty level {difficulty}")
            result = play_guess_game(difficulty)
        elif game_choice == '3':
            print(f"Starting Currency Roulette with difficulty level {difficulty}")
            result = play_currency_roulette_game(difficulty, api_key)

        if result:
            points_won = difficulty * 5  # Points won based on difficulty level
            new_score = get_player_score(username) + points_won
            add_score(username, new_score)  # Add the new score to the user's file
            print("Congratulations! You won!")
            print(f"If you want to view your score, go to: http://localhost:5000/scores/{username}")
        else:
            print("Sorry, you lost. Better luck next time.")

        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            break

if __name__ == "__main__":
    username = input("Enter your name: ")
    api_key = "3b0a56867dae17a85e74e4de"  # Assurez-vous que la clé API est définie ici
    welcome(username)
    start_play(username, api_key)