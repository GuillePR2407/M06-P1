from Categoria import Categoria
from Registre import Registre
from Article import Article
from Llista import Llista

# Crear objetos de prueba
article1 = Article("Mountain Dew")
article2 = Article("Doritos")
categoria1 = Categoria("Aperitivos")
categoria2 = Categoria("Huevos")
registre1 = Registre(article1, 10)
registre2 = Registre(article2, 5)

# Crear una lista
llista = Llista()

# Pruebas de creación y manejo de registros y categorías
llista.create_registre(registre1)
llista.create_registre(registre2)

llista.create_categoria(categoria1)

print("Registros antes de la eliminación:")
print(llista.get_registres())

# Eliminar un registro
llista.delete_registre("Mountain Dew")

print("Registros después de la eliminación:")
print(llista.get_registres())

# Pruebas de deserialización y serialización
llista.desa_a_disc("data_test.json")

# Crear una nueva instancia de Llista para cargar los datos desde el archivo
llista_nueva = Llista()
llista_nueva.llegeix_de_disc("data_test.json")

print("Registros cargados desde el archivo:")
print(llista_nueva.get_registres())

# Pruebas de lectura de categoría
try:
    categoria = llista_nueva.read_categoria("Aperitivos")
    print("Categoría encontrada:", categoria.get_nom())
except ValueError as e:
    print(e)

# Pruebas de actualización de registro y categoría
try:
    llista_nueva.update_registre("Doritos", 7)  # Nombre del artículo y nueva cantidad
    llista_nueva.update_categoria(Categoria(categoria1.get_nom()))
    print("Registro y categoría actualizados:")
    print(llista_nueva.get_registres())
    print(llista_nueva.read_categoria("Aperitivos").get_nom())
except ValueError as e:
    print(e)
