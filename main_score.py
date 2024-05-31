import os
from games.memory_game import play_memory_game
from games.guess_game import play as play_guess_game
from games.currency_roulette_game import play as play_currency_roulette_game
from score import add_score, get_player_score

def welcome(username):
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")

def start_play(username):
    current_score = get_player_score(username)
    if current_score is not None:
        print(f"Your current score is: {current_score}")
    else:
        print("No score found for this user.")

    while True:
        print("Please choose a game to play:")
        print("1. Memory Game - a sequence of numbers will appear for 3 second and you have to guess it back.")
        print("2. Guess Game - guess a number and see if you chose like the computer.")
        print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

        game_choice = input("Enter the number corresponding to the game you want to play: ")

        if game_choice not in ['1', '2', '3']:
            print("Invalid choice. Please enter a number between 1 and 3.")
            continue

        difficulty = input("Enter the difficulty level (1-5): ")

        if difficulty not in ['1', '2', '3', '4', '5']:
            print("Invalid difficulty level. Please enter un numéro entre 1 et 5.")
            continue

        if game_choice == '1':
            print("Starting Memory Game with difficulty level", difficulty)
            result = play_memory_game(int(difficulty))
        elif game_choice == '2':
            print("Starting Guess Game with difficulty level", difficulty)
            result = play_guess_game(int(difficulty))
        elif game_choice == '3':
            print("Starting Currency Roulette with difficulty level", difficulty)
            result = play_currency_roulette_game(int(difficulty))

        if result:
            print("Congratulations! You won!")
            new_score = current_score + (int(difficulty) * 3) + 5 if current_score else (int(difficulty) * 3) + 5
            add_score(username, new_score)
            print("If you want to view your score, go to: http://localhost:5000/scores/{}".format(username))
        else:
            print("Sorry, you lost. Better luck next time.")

        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            break
