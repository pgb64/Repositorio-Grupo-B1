def obtener_definicion(tema):
    definicones = {
        'Microsoft: Entidad vampírica que intenta monopolizar el mercado de la informática',
        'Pycharm: Aplicacion de programacion copia de la amada VSC'
    }
    return definicones.get(tema.lower(), "Definición no encontrada")

if __name__ == "__main__":
    tema = input("Ingrese un tema: ")
    print(obtener_definicion(tema))