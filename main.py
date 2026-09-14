from funciones.gestor_autos import crear_auto
from funciones.gestor_autos import listar_autos
from funciones.gestor_autos import calcular_antiguedad
from funciones.gestor_autos import agregar_color
from funciones.gestor_autos import ver_colores


lista_autos = []
opcion = ""

while opcion != "0":
    print("\nSISTEMA DE AUTOS")
    print("1. Crear auto")
    print("2. Listar autos")
    print("3. Calcular antigüedad")
    print("4. Agregar color a la lista")
    print("5. Ver lista de colores")
    print("0. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        marca = input("Ingresá la marca: ")
        modelo = input("Ingresá el modelo: ")
        anio = int(input("Ingresá el año: "))

        auto = crear_auto(marca, modelo, anio)
        lista_autos.append(auto)

    elif opcion == "2":
        listar_autos(lista_autos)

    elif opcion == "3":
        listar_autos(lista_autos)

        if len(lista_autos) > 0:
            id_auto = int(input("Ingresá el ID del auto: "))

            if id_auto >= 0 and id_auto < len(lista_autos):
                antiguedad = calcular_antiguedad(lista_autos[id_auto])
                print("La antigüedad del auto es de", antiguedad, "años.")
            else:
                print("Ese ID no existe.")

    elif opcion == "4":
        listar_autos(lista_autos)

        if len(lista_autos) > 0:
            id_auto = int(input("Ingresá el ID del auto: "))

            if id_auto >= 0 and id_auto < len(lista_autos):
                color = input("Ingresá un color: ")
                agregar_color(lista_autos[id_auto], color)
            else:
                print("Ese ID no existe.")

    elif opcion == "5":
        listar_autos(lista_autos)

        if len(lista_autos) > 0:
            id_auto = int(input("Ingresá el ID del auto: "))

            if id_auto >= 0 and id_auto < len(lista_autos):
                ver_colores(lista_autos[id_auto])
            else:
                print("Ese ID no existe.")

    elif opcion == "0":
        print("Programa finalizado.")

    else:
        print("Opción incorrecta.")
