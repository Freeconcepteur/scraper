from pymongo import MongoClient

def find_articles_with_keyword(db_name, collection_name, keyword):
    client = MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    collection = db[collection_name]

    query = {"title": {"$regex": keyword, "$options": "i"}}  # Recherche insensible à la casse
    articles = collection.find(query)

    return list(articles)

# Utilisation de la fonction
db_name = "inserm_articles"
collection_name = "articles"
keyword = "trouble"

found_articles = find_articles_with_keyword(db_name, collection_name, keyword)

for article in found_articles:
    print(article)
