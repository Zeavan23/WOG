from main_score import welcome, start_play

def main():
    username = input("Enter your name: ")
    api_key = "3b0a56867dae17a85e74e4de"  # Assurez-vous que l'API key est définie ici
    welcome(username)
    start_play(username, api_key)

if __name__ == "__main__":
    main()
