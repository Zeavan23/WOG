# currency_roulette_game.py
import requests
import random

def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Request failed with status:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error retrieving exchange rates:", e)
        return None

def generate_usd_amount():
    return random.randint(1, 101)

def play(difficulty):
    exchange_rate_data = get_exchange_rate()
    if exchange_rate_data:
        usd_amount = generate_usd_amount()
        exchange_rate = exchange_rate_data.get('rates').get('ILS')
        correct_amount_in_ils = usd_amount * exchange_rate
        print("The amount in USD is:", usd_amount)
        user_guess = float(input("Guess the amount in ILS: "))
        print("The correct amount in ILS is:", correct_amount_in_ils)
        if abs(user_guess - correct_amount_in_ils) <= difficulty * 10:
            return True
        else:
            return False
    else:
        print("Sorry, something went wrong. Please try again later.")
        return False

if __name__ == "__main__":
    play(1)
