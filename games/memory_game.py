import time
import random
import sys

def display_sequence(sequence):
    print(f"Remember these numbers for 3 seconds:")
    print(sequence)
    time.sleep(3)
    clear_console()
    print("Now enter the numbers you saw:")

def clear_console():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def get_list_from_user(correct_sequence):
    if sys.stdin.isatty():
        return input().strip()
    else:
        return sys.stdin.read().strip()

def is_list_equal(seq1, seq2):
    return seq1 == seq2

def generate_sequence(difficulty):
    return [random.randint(1, 100) for _ in range(difficulty)]

def play_memory_game(difficulty):
    sequence = generate_sequence(difficulty)
    display_sequence(sequence)
    user_input = get_list_from_user(sequence)

    if user_input == '':
        return False
    else:
        user_numbers = [int(num) for num in user_input.split() if num.isdigit()]
        return is_list_equal(sequence, user_numbers)
