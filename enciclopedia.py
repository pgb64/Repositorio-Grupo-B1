def obtener_definicion(tema):
    definicones = {
        # Aquí cada persona agregará su tema y definición
    }
    return definicones.get(tema.lower(), "Definición no encontrada")

if __name__ == "__main__":
    tema = input("Ingrese un tema: ")
    print(obtener_definicion(tema))