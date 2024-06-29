# app.py
from flask import Flask, render_template_string
from utils import get_player_score

app = Flask(__name__)

@app.route('/scores/<player_name>')
def score_server(player_name):
    score = get_player_score(player_name)
    if score is not None:
        return render_template_string(
            """
            <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>{{ player_name }}'s score is {{ score }}</h1>
            </body>
            </html>
            """,
            player_name=player_name,
            score=score
        )
    else:
        return render_template_string(
            """
            <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>ERROR: Failed to retrieve score for {{ player_name }}</h1>
            </body>
            </html>
            """,
            player_name=player_name
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8777)  # Port 5000 pour l'application Flask
