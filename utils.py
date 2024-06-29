import os

SCORES_FILE_NAME = "scores/Scores.txt"

def get_player_score(username):
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, "r") as file:
            scores = file.readlines()
            for score in scores:
                user, points = score.strip().split(":")
                if user == username:
                    return int(points)
    return None

def add_score(username, score):
    scores = {}
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, "r") as file:
            scores = dict(line.strip().split(":") for line in file.readlines())

    scores[username] = str(score)

    with open(SCORES_FILE_NAME, "w") as file:
        for user, points in scores.items():
            file.write(f"{user}:{points}\n")
