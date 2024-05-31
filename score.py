import os

SCORES_DIRECTORY = "scores"

def add_score(player_name, new_score):
    try:
        scores_file = os.path.join(SCORES_DIRECTORY, f"{player_name}.txt")
        with open(scores_file, 'w') as file:
            file.write(str(new_score))
    except Exception as e:
        print(f"Failed to add score for {player_name}: {e}")

def get_player_score(player_name):
    try:
        scores_file = os.path.join(SCORES_DIRECTORY, f"{player_name}.txt")
        if os.path.exists(scores_file):
            with open(scores_file, 'r') as file:
                score = int(file.read())
            return score
        else:
            return None
    except Exception as e:
        print(f"Error reading score for {player_name}: {str(e)}")
        return None
