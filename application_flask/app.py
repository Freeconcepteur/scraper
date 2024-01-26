import random
from flask import Flask, render_template
import json
import os

app = Flask(__name__)


# Configuration de la connexion MongoDB 
# db = client["inserm_articles"]
# collection = db["articles"]


# Configurer le chemin par défaut pour 'resultats.jsonl'
app.config['RESULTATS_JSONL_PATH'] = os.path.join(
    app.root_path, 
    'data',
    'resultats.jsonl')


def lire_jsonl(chemin_fichier):
    with open(chemin_fichier, 'r') as file:
        for ligne in file:
            yield json.loads(ligne)


@app.route('/')
def get_random_item():
    # Utiliser le chemin à partir de la configuration Flask
    chemin_fichier = app.config['RESULTATS_JSONL_PATH']
    articles = list(lire_jsonl(chemin_fichier))
    article_aleatoire = random.choice(articles)
    return render_template('random_item.html', item=article_aleatoire)


if __name__ == '__main__':
    app.run(debug=True)
