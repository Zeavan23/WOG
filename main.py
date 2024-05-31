from main_score import welcome, start_play

def main():
    username = input("Enter your name: ")
    welcome(username)
    start_play(username)

if __name__ == "__main__":
    main()
