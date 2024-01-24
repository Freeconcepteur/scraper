from flask import Flask, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
import random
from flask import Flask, render_template
import json

app = Flask(__name__)

# Configuration de la connexion MongoDB (ajustez les paramètres selon votre configuration)
# client = MongoClient("mongodb://localhost:27017/")
# db = client["inserm_articles"]
# collection = db["articles"]

def lire_jsonl(chemin_fichier):
    with open(chemin_fichier, 'r') as file:
        for ligne in file:
            yield json.loads(ligne)


@app.route('/')
def get_random_item():
    articles = list(lire_jsonl('data/resultats.jsonl'))
    article_aleatoire = random.choice(articles)
    return render_template('random_item.html', item=article_aleatoire)

if __name__ == '__main__':
    app.run(debug=True)
