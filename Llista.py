from Categoria import Categoria
from Registre import Registre
from Article import Article 
import json

class Llista:
    def __init__(self):
        self.registres = []
        self.categories = []

    def get_registres(self):
        registres_dict = []
        for registre in self.registres:
            registres_dict.append(registre.to_dict())
        return registres_dict

    def create_registre(self, registre):
        if self.read_registre(registre.article.get_nom()) is None:
            self.registres.append(registre)
            return registre
        else:
            raise ValueError("Nom de l'article ja existeix")

    def read_registre(self, nom_article):
        for registre in self.registres:
            if registre.article.get_nom() == nom_article:
                return registre
            return None

    def update_registre(self, nom_article, nova_quantitat):
        for registre in self.registres:
            if registre.article.get_nom() == nom_article:
                registre.set_quantitat(nova_quantitat)
                return registre
        raise ValueError("No s'ha trobat l'article")


    def delete_registre(self, nom_article):
        for registre in self.registres:
            if registre.article.get_nom() == nom_article:
                self.registres.remove(registre)
                return
        raise ValueError("No s'ha trobat l'article")


    def create_categoria(self, categoria):
        if self.read_categoria(categoria.get_nom()) is None:
            self.categories.append(categoria)
            return categoria
        else:
            raise ValueError("El nom de la categoria ja existeix")


    def read_categoria(self, nom_categoria):
        for categoria in self.categories:
            if categoria.get_nom() == nom_categoria:
                return categoria
            else:
                raise ValueError("No s'ha trobat la categoria")


    def update_categoria(self, categoria):
        for i, c in enumerate(self.categories):
            if c.get_nom() == categoria.get_nom():
                self.categories[i] = categoria
                return categoria
        raise ValueError("No s'ha trobat la categoria")

    def delete_categoria(self, nom_categoria):
        for categoria in self.categories:
            if categoria.get_nom() == nom_categoria:
                self.categories.remove(categoria)
                return
        raise ValueError("No s'ha trobat la categoria")

    def desa_a_disc(self, filename='data.json'):
        data = {
            'registres': [r.to_dict() for r in self.registres],
            'categories': [c.to_dict() for c in self.categories]
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def llegeix_de_disc(self, filename='data.json'):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.registres = [Registre.from_dict(r) for r in data['registres']]
                self.categories = [Categoria.from_dict(c) for c in data['categories']]
                print(data['registres'])
                print(data['categories'])
        except FileNotFoundError:
            # Si el archivo no existe todavía, se crea vacío.
            self.registres = []
            self.categories = []