import scrapy


class ArticlesSpider(scrapy.Spider):
    name = "articles_inserm"
    start_urls = [
        "https://presse.inserm.fr/dans-lactualite/communiques-dossiers/",
        "https://presse.inserm.fr/dans-lactualite/breves/",
        "https://presse.inserm.fr/dans-lactualite/cest-dans-lair/"
    ]

    custom_settings = {
        'FEED_FORMAT': 'jsonlines',  # Format de sortie JSON Lines
        'FEED_URI': '../resultats.jsonl'  # Nom de fichier pour la sortie
    }

    def parse(self, response):
        # Parcourir chaque article dans la page
        for article in response.css("#posts-list .row.border"):
            # Extraire et structurer les données
            yield {
                "title": article.css(".col-md-9 a h2::text").get(),
                "synopsis": article.css(".col-md-9 p::text").get(),
                "link": article.css(".col-md-9 a::attr(href)").get()
            }


# Suivre les liens de pagination (si applicable)
        next_page = response.css("# posts-list > div > div > div > div.pagination03 > div > a.nextpostslink::attr(href)").get()#posts-list > div > div > div > div.pagination03 > div > a.nextpostslink
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
