def obtener_definicion(tema):
    definicones = {
        'Pycharm': 'Aplicacion de programacion copia de la amada VSC',
        'Microsoft': 'Entidad vampírica que intenta monopolizar el mercado de la informática',
        'Windows': 'Sistema operativo en tipo de archivo NFTS incompatible con Linux'
    }
    return definicones.get(tema.lower(), "Definición no encontrada")

if __name__ == "__main__":
    tema = input("Ingrese un tema: ")
    print(obtener_definicion(tema))
