import random
import os

os.system('cls')

estadisticas = {
    'partidas': 0, 'racha': 0, 'mejorRacha': 0,
    'aciertos': 0, 'fallos': 0
}

palabras = []
palabrasNoEncontradas = []
letras = {
    'A': '', 'B': '', 'C': '', 'D': '',
    'E': '', 'F': '', 'G': '', 'H': '',
    'I': '', 'J': '', 'K': '', 'L': '',
    'M': '', 'N': '', 'O': '', 'P': '',
    'Q': '', 'R': '', 'S': '', 'T': '',
    'U': '', 'V': '', 'W': '', 'X': '',
    'Y': '', 'Z': ''
}
palabrasUsadas = {
    
}
terminar = False

def mostrarResultados():
    porcentajeVictorias = (estadisticas['aciertos']/(estadisticas['partidas']))*100
    print("Estadísticas:\
           \nJugadas: %i | Victorias: %d (Porcentaje) | Racha Actual: %i | Mejor Racha: %i"
           % (estadisticas['partidas'], porcentajeVictorias, estadisticas['racha'], estadisticas['mejorRacha']))
    print("Distribución:")
    i = 1
    while i <= cantidadIntentos:
        print("%i: %i" % (i, estadisticas[i.__str__()]))
        i += 1
    print("Fallos: %i" % (estadisticas['fallos']))

def setLetras():
    cantidadLetras = int(input("Ingrese la cantidad de letras para las palabras (El valor debe ser un número entero desde el 5 al 8): "))
    while cantidadLetras < 5 or cantidadLetras > 8:
        cantidadLetras = int(input("¡Cantidad de letras no posible!\nIngrese la cantidad de letras para las palabras (El valor debe ser un número entero desde el 5 al 8): "))
    os.system('cls')
    
    with open("posiblesPalabras%iletras.txt" % (cantidadLetras), "r") as archivo:
        for x in archivo:
            palabras.append(x.strip())
            
    return cantidadLetras

def setIntentos():
    cantidadIntentos = int(input("Ingrese la cantidad de intentos para adivinar (El valor debe ser un número entero desde el 3 al 9): "))
    while cantidadIntentos < 3 or cantidadIntentos > 9:
        cantidadIntentos = int(input("¡Cantidad de intentos no posible!\nIngrese la cantidad de intentos para adivinar (El valor debe ser un número entero desde el 3 al 9): "))
    os.system('cls')

    i = 1
    while i <= cantidadIntentos:
        estadisticas[i.__str__()] = 0
        i += 1
        
    return cantidadIntentos
        
cantidadLetras = setLetras()
cantidadIntentos = setIntentos()      

def setDificultad():
    aceptar = ''
    while aceptar != 's':
        print("¿Está seguro que quiere ir con esta dificultad?\n\
            Cantidad de letras: %i\n\
            Cantidad de intentos: %i\n\
            Advertencia: La dificultad no puede ser cambiada a menos que se reinicie el programa."
            % (cantidadLetras, cantidadIntentos))
        aceptar = input("¿Desea comenzar con el juego? (s = sí): ").lower()
        os.system('cls')

setDificultad()

def compararPalabras(palabraIngresada):
    i = 0
    coincidencias = ''
    for x in palabraIngresada:
        if x == palabra[i]:
            coincidencias += '='
            letras[x] = 'Coincide'
        elif x in palabra:
            coincidencias += '-'
            letras[x] = 'Contiene'
        else:
            coincidencias += ' '
            letras[x] = 'No se encuentra'
        i += 1
    return coincidencias

def imprimirPalabraConEspacios(palabra):
    palabraConEspacios = ''
    for x in palabra:
        palabraConEspacios += x + ' '
    return palabraConEspacios

def acertar():
    print("\nACERTASTE!!!")
    estadisticas['aciertos'] += 1
    estadisticas[intento.__str__()] += 1
    if estadisticas['mejorRacha'] == estadisticas['racha']:
        estadisticas['mejorRacha'] += 1
    estadisticas['racha'] += 1

def fallar():
    print("\nFALLASTE!!!")
    print("La palabra era %s" % (palabra))
    estadisticas['fallos'] += 1
    estadisticas['racha'] = 0

def imprimirLetras():
    print("Letras Usadas: ")
    i = 0
    for x in letras:
        print("%s: %s\n" % (x, letras[x]), end=' ')
        i += 1
    print()

def imprimirPalabrasUsadas():
    print("Palabras usadas: ")
    for x in palabrasUsadas:
        print("%s\n%s\n" % (x, palabrasUsadas[x]))

def añadirPalabras(palabra):
    with open("posiblesPalabras%iletras.txt" % (cantidadLetras), "a+") as archivo:
        archivo.write(palabra + '\n')
        palabras.append(palabra.strip())
        palabrasNoEncontradas.remove(x)

def registrarEstadisticas():
    with open("registroEstadisticas.txt", "a+") as archivo:
        porcentajeVictorias = (estadisticas['aciertos']/(estadisticas['partidas']))*100
        archivo.write("Estadisticas:\n")
        archivo.write("Jugadas: %i | Victorias: %d (Porcentaje) | Racha Actual: %i | Mejor Racha: %i" % (estadisticas['partidas'], porcentajeVictorias, estadisticas['racha'], estadisticas['mejorRacha']))
        archivo.write("\nDistribucion\n")
        i = 1
        while i <= cantidadIntentos:
            archivo.write("%i: %i\n" % (i, estadisticas[i.__str__()]))
            i += 1
        archivo.write("Fallos: %i" % (estadisticas['fallos']))
        archivo.write('\n\n')

while terminar == False:
    palabra = palabras[random.randrange(0, len(palabras))]
    estadisticas['partidas'] += 1
    intento = 1
    while intento <= cantidadIntentos:
        os.system('cls')
        if intento > 1:
            imprimirPalabrasUsadas()
            print()
            imprimirLetras()
        palabraIngresada = input("Ingrese una palabra de %i letras: " % (cantidadLetras)).upper()
        while palabraIngresada not in palabras:
            if len(palabraIngresada) == cantidadLetras:
                palabrasNoEncontradas.append(palabraIngresada)
            palabraIngresada = input("Esa palabra no se encuentra entre la lista de posibles palabras de %i letras\nIngrese una palabra de %i letras: " % (cantidadLetras, cantidadLetras)).upper()
        
        palabraConEspacios = imprimirPalabraConEspacios(palabraIngresada)
        print(palabraConEspacios)
        coincidencias = imprimirPalabraConEspacios(compararPalabras(palabraIngresada))
        print(coincidencias)

        if palabraIngresada == palabra:
            acertar()
            intento = 999
        elif intento == cantidadIntentos:
            fallar()
        elif intento < cantidadIntentos:
            palabrasUsadas[palabraConEspacios] = coincidencias
        
        intento += 1
        print()
        
    mostrarResultados()
    
    for x in palabrasNoEncontradas:
        respuesta = input("¿Le gustaría añadir la palabra %s a la lista de posibles palabras? (s = sí): " % (x)).lower()
        if respuesta == 's':
            añadirPalabras(x)
        else:
            print("La palabra %s no se ha añadido a la lista de posibles palabras." % (x))
            palabrasNoEncontradas.remove(x)
    
    if input("¿Desea continuar jugando? (s = sí): ").lower() != 's':
        terminar = True
        registrarEstadisticas()
