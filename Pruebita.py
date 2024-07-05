juegos = []
import csv

#Nombre, Jugadores, Valor, Consola, year
with open("juegos.csv", "r", newline='', encoding="utf-8-sig") as arch:
    info = csv.reader(arch)
    for linea in info:
        nombre = linea[0]
        jugadores = int(linea[1])
        valor = float(linea[2])
        consola = linea[3]
        year = int(linea[4])
    #Crear el diccionario
    
        datos = {
            "nombre": nombre,
            "jugadores": jugadores,
            "valor": valor,
            "consola": consola,
            "year": year
        }
        juegos.append(datos)
        
def Filtro_jugador():
    modalida = input("Desea juegos SinglePlayer o MultiPlayer (s/m)?: ").lower()
    if modalida == "s":
        filtrar = []
        for sm in juegos:
            if sm["jugadores"] == 1:
                filtrar.append(sm)
                if len(filtrar) == 10:
                    break
    if modalida == "m":
        filtrar = []
        for sm in juegos:
            if sm["jugadores"] != 1:
                filtrar.append(sm)
                if len(filtrar) == 10:
                    break
    return filtrar

def  Filtro_precio():
    precio_minimo = float(input("Ingrese Precio minimo: "))
    precio_maximo = float(input("Ingrese Precio maximo: "))
    filtrar = []
    for cash in juegos:
        if precio_minimo < cash["valor"] < precio_maximo:
            filtrar.append(cash)
            if len(filtrar) == 10:
                break
    if not filtrar:
        print("[ERROR] No hay juegos dentro de ese rango!!!")
    return filtrar

def Filtro_consola_y_año():
    filtrar = []
    consolas = input("Ingrese una consola (Nintendo DS, Nintendo Wii, PlayStation 3, Sony PSP, X360): ")
    fecha = int(input("Ingrese un año (2004 hasta 2008): "))
    for console in juegos:
        if consolas in console["consola"] and fecha == console["year"]:
            filtrar.append(console)
            if len(filtrar) == 10:
                break
    # Ordenar los juegos filtrados por nombre
    for i in range(len(filtrar)):
        for j in range(i + 1, len(filtrar)):
            if filtrar[i]["nombre"] > filtrar[j]["nombre"]:
                filtrar[i], filtrar[j] = filtrar[j], filtrar[i]
    return filtrar

def Escribir_archivo(filtrar):
    with open("Filtro_juegos.txt", 'w', encoding='utf-8') as archivo:
        for juego in filtrar:
            archivo.write(f"{juego['nombre']}, {juego['consola']}, {juego['year']}, ${juego['valor']}\n")
    print("[!] Archivo creado con exito...")

def Menu_principal():
    print("***MENU PRINCIPAL***")
    print("1. Filtro jugador")
    print("2. Filtro precio")
    print("3. Filtro consola y año")
    print("4. Escribir archivo")
    print("5. Salir")

while True:
    Menu_principal()
    opcion = input("Ingrese la opcion deseada: ")

    if opcion == "1":
        print("[+] FILTRO JUGADOR!")
        juegos_filtrados = Filtro_jugador()
        for juego in juegos_filtrados:
            print(juego["nombre"])
    elif opcion == "2":
        print("[+] FILTRO PRECIO!")
        juegos_filtrados = Filtro_precio()
        for juego in juegos_filtrados:
            print(juego["nombre"])
    elif opcion == "3":
        print("[+] FILTRO CONSOLA Y AÑO")
        juegos_filtrados = Filtro_consola_y_año()
        for juego in juegos_filtrados:
            print(juego["nombre"])
    elif opcion == "4":
        print("[+] ESCRIBIR ARCHIVO")
        if 'juegos_filtrados' in locals() and juegos_filtrados:
            Escribir_archivo(juegos_filtrados)
        else:
            print("[ERROR] No hay juegos filtrados!!!")
    elif opcion == "5":
        print("[!] Saliendo del programa...")
        break
    else:
        print("[ERROR] Ingrese una opcion valida!!!")