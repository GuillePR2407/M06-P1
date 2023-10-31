class Categoria:
    def __init__(self, nom):
        self.nom = nom
        self.articles = []

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_articles(self):
        return self.articles

    def add_article(self, article):
        self.articles.append(article)
        return article

    def delete_article(self, nom_article):
        for article in self.articles:
            if article.get_nom() == nom_article:
                self.articles.remove(article)
                print(f"El artículo '{nom_article}' ha sido eliminado de la categoría.")
                return
        print(f"No se encontró un artículo con el nombre '{nom_article}' en la categoría.")