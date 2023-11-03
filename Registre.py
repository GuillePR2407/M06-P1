from Article import Article

class Registre:
    def __init__(self, article, quantitat):
        self.article = article
        self.quantitat = quantitat

    def get_quantitat(self):
        return self.quantitat

    def set_quantitat(self, quantitat):
        if quantitat >= 0:
            self.quantitat = quantitat
        else:
            print("no es pot")
    
    def to_dict(self):
        return {
            'article': self.article.to_dict(),
            'quantitat': self.quantitat
        }

    @classmethod
    def from_dict(cls, data):
        # Verifica si 'article' és un diccionari, si ho és, crea una instància de la classe Article
        if isinstance(data['article'], dict):
            article = Article.from_dict(data['article'])
        else:
            # Si no és un diccionari, assumeix que és ja una instància de la classe Article
            article = data['article']

        return cls(article, data['quantitat'])