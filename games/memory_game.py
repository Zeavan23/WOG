# memory_game.py
import random
import time

def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]

def display_sequence(sequence):
    print("Remember these numbers for 3 seconds:")
    print(sequence)
    time.sleep(3)
    print("\n" * 100)

def get_list_from_user(difficulty):
    print("Now enter the numbers you saw:")
    user_input = input().split()
    user_input = [int(num) for num in user_input if num.isdigit()]
    while len(user_input) != difficulty:
        print("Invalid input. Please enter exactly", difficulty, "numbers separated by spaces.")
        user_input = input().split()
        user_input = [int(num) for num in user_input if num.isdigit()]
    return user_input

def is_list_equal(seq1, seq2):
    return seq1 == seq2

def play_memory_game(difficulty):
    sequence = generate_sequence(difficulty)
    display_sequence(sequence)
    user_input = get_list_from_user(difficulty)
    return is_list_equal(sequence, user_input)

