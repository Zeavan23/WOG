import random
import os
import time

def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]

def display_sequence(sequence):
    clear_console()
    print("Remember these numbers for 3 seconds:")
    print(sequence)
    time.sleep(3)
    clear_console()

def get_list_from_user(difficulty):
    print("Now enter the numbers you saw:")
    time.sleep(3)
    clear_console()
    return input().strip()

def is_list_equal(seq1, seq2):
    return seq1 == seq2

def play_memory_game(difficulty):
    sequence = generate_sequence(difficulty)
    display_sequence(sequence)
    user_input = get_list_from_user(difficulty)

    if user_input == '':
        return False
    else:
        user_numbers = [int(num) for num in user_input.split() if num.isdigit()]
        return is_list_equal(sequence, user_numbers)

if __name__ == "__main__":
    play_memory_game(1)
