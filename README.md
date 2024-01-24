# Scraper 

Ce script permet de crawler et d'indexer les articles du site presse.inserm.fr et de les afficher via une application Flask. L'indexation se fait en deux modes : en stockant dans une base de données MongoDB et dans un fichier JSONL (`resultats.jsonl`).

## Prérequis

- Docker
- MongoDB
- Python 3
- Flask
- Scrapy

## Installation

### Étape 1 : Configuration de MongoDB

Utilisez Docker pour créer une base de données MongoDB :

```bash
docker run --name <nom_de_la_base> -p 27017:27017 -d mongo
```

Votre base de données devrait être accessible à l'adresse indiquée.

### Étape 2 : Configuration de l'Environnement

1. Créez un environnement virtuel.
2. Installez les dépendances nécessaires.

### Étape 3 : Lancement du Scraper

Dans le répertoire /presse_inserm, exécutez la commande suivante :

```bash
scrapy crawl articles_inserm
```

Cela générera un fichier resultats.jsonl à la racine du projet.

### Étape 4 : Affichage des Données avec Flask

1. Déplacez le fichier resultats.jsonl dans /application_flask/data/.
2. Dans le répertoire /application_flask, exécutez :

```bash
python3 app.py
```

Votre application Flask devrait maintenant afficher les données scrapées.