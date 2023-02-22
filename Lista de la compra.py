text_1 = "Introduce un producto [{} para terminar][{} para abrir Lista]\n"
SALIDA = "SALIR"
LISTA = "LISTA"
lista_productos = ["pollo", "pan", "huevos", "carne", "pescado", "leche", "verduras", "coco"]

def file(lista_compra):
    name_file = input("Introduce el nombre del fichero.\n")
    with open(name_file + ".txt", "w") as fichero:
        fichero.write("---LISTA DE LA COMPRA---\n")
        fichero.write("\n".join(lista_compra))


def preguntar_prod_user():
    producto_elegido = input(text_1.format(SALIDA, LISTA))

    while producto_elegido.lower() not in lista_productos and producto_elegido != SALIDA and producto_elegido != LISTA:
        print("Este producto no existe.")
        producto_elegido = input(text_1.format(SALIDA, LISTA))
    return producto_elegido

def main():
    lista_compra = []
    input_user = preguntar_prod_user()


    while input_user != SALIDA:
        
        print("\n".join(lista_compra))
        input_user = preguntar_prod_user()

    file(lista_compra)


if __name__ == "__main__":
    main()