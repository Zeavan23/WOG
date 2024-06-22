import requests
import random

def get_exchange_rate(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['conversion_rates']['ILS']
        else:
            print("Request failed with status:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error retrieving exchange rates:", e)
        return None

def generate_usd_amount():
    return random.randint(1, 101)

def play(difficulty, api_key):
    exchange_rate = get_exchange_rate(api_key)
    if exchange_rate:
        usd_amount = generate_usd_amount()
        correct_amount_in_ils = usd_amount * exchange_rate
        print(f"The amount in USD is: {usd_amount}")

        try:
            user_guess = float(input("Guess the amount in ILS: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return False

        print(f"The correct amount in ILS is: {correct_amount_in_ils:.2f}")

        return abs(user_guess - correct_amount_in_ils) <= difficulty * 10
    else:
        print("Sorry, something went wrong. Please try again later.")
        return False

if __name__ == "__main__":
    api_key = "3b0a56867dae17a85e74e4de"
    play(1, api_key)
