def obtener_definicion(tema):
    definicones = {
        'Microsoft': 'Entidad vampírica que intenta monopolizar el mercado de la informática'
    }
    return definicones.get(tema.lower(), "Definición no encontrada")

if __name__ == "__main__":
    tema = input("Ingrese un tema: ")
    print(obtener_definicion(tema))
