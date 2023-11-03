from Categoria import Categoria
from Registre import Registre
from Article import Article 
import json

class Llista:
    def __init__(self):
        self.registres = []
        self.categories = []

    def get_registres(self):
        return self.registres

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

    def update_registre(self, registre):
        for i, r in enumerate(self.registres):
            if r.article.get_nom() == registre.article.get_nom():
                self.registres[i] = registre
                return registre
        return None


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

    def desa_a_disc(self):
        pass

    def llegeix_de_disc(self):
        pass