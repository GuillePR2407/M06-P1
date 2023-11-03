from Article import Article

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
                print(f"L'article '{nom_article}' ha sigut eliminat de la categoría.")
                return
        print(f"No s'ha trobat un article amb el nombre '{nom_article}' en la categoría.")

    def to_dict(self):
        return {
            'nom': self.nom,
            'articles': [article.to_dict() for article in self.articles]
        }

    @classmethod
    def from_dict(cls, data):
        categoria = cls(data['nom'])
        categoria.articles = [Article.from_dict(article_data) for article_data in data['articles']]
        return categoria