def crear_auto(marca, modelo, anio):
    auto = {
        "marca": marca,
        "modelo": modelo,
        "anio": anio,
        "colores": []
    }

    print("Auto creado correctamente.")
    return auto


def listar_autos(lista):
    if len(lista) == 0:
        print("No hay autos cargados.")
        return

    for i in range(len(lista)):
        auto = lista[i]
        print("ID:", i)
        print("Marca:", auto["marca"])
        print("Modelo:", auto["modelo"])
        print("Año:", auto["anio"])
        print("Colores:", auto["colores"])
        print("--------------------")


def calcular_antiguedad(auto):
    anio_actual = 2026
    antiguedad = anio_actual - auto["anio"]
    return antiguedad


def agregar_color(auto, color):
    auto["colores"].append(color)
    print("Color agregado correctamente.")


def ver_colores(auto):
    if len(auto["colores"]) == 0:
        print("Este auto todavía no tiene colores cargados.")
    else:
        print("Colores del auto:")
        for color in auto["colores"]:
            print("-", color)
