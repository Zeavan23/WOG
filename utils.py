import os

SCORES_DIRECTORY = os.path.join(os.path.dirname(__file__), "scores")

# Assurez-vous que le répertoire des scores existe
if not os.path.exists(SCORES_DIRECTORY):
    os.makedirs(SCORES_DIRECTORY)


def add_score(player_name, new_score):
    try:
        scores_file = os.path.join(SCORES_DIRECTORY, f"{player_name}.txt")

        # Vérifiez si le fichier de score existe déjà
        if os.path.exists(scores_file):
            current_score = get_player_score(player_name)  # Obtenir le score actuel
            if current_score is not None:
                new_score += current_score  # Ajouter le nouveau score au score actuel
        else:
            # Si le fichier de score n'existe pas, initialiser le score à zéro
            with open(scores_file, 'w') as file:
                file.write("0")

        # Écrire le nouveau score dans le fichier
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
            # Si le fichier de score n'existe pas encore, retourner 0
            with open(scores_file, 'w') as file:
                file.write("0")
            return 0

    except Exception as e:
        print(f"Error reading score for {player_name}: {str(e)}")
        return None
