import random
import time
import os

os.system('cls')

estJug1 = {
    'partidas': 0, 'racha': 0, 'mejorRacha': 0,
    'aciertos': 0, 'fallos': 0,
    'fin': 0.0, 'tiempo': []
}
estJug2 = {
    'partidas': 0, 'racha': 0, 'mejorRacha': 0,
    'aciertos': 0, 'fallos': 0,
    'fin': 0.0, 'tiempo': []
}
estadisticasJugador = [estJug1, estJug2]
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
        estadisticasJugador[0][i.__str__()] = 0
        estadisticasJugador[1][i.__str__()] = 0
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

def compararPalabras(palabraIngresada):
    i = 0
    coincidencias = ''
    for x in palabraIngresada:
        if x == palabra[i]:
            coincidencias += '='
        elif x in palabra and x != palabra[i]:
            coincidencias += '-'
        else:
            coincidencias += '~'
        letras[x] = coincidencias[i]
        i += 1
    return coincidencias

def imprimirPalabraConEspacios(palabra):
    palabraConEspacios = ''
    for x in palabra:
        palabraConEspacios += x + ' '
    return palabraConEspacios

def acertar(jug):
    print("\nACERTASTE!!!")
    estadisticasJugador[jug]['aciertos'] += 1
    estadisticasJugador[jug][intento.__str__()] += 1
    if estadisticasJugador[jug]['mejorRacha'] == estadisticasJugador[jug]['racha']:
        estadisticasJugador[jug]['mejorRacha'] += 1
    estadisticasJugador[jug]['racha'] += 1

def fallar(jug):
    print("\nFALLASTE!!!")
    print("La palabra era %s" % (palabra))
    estadisticasJugador[jug]['fallos'] += 1
    estadisticasJugador[jug]['racha'] = 0

def imprimirPalabrasUsadas():
    print("Palabras usadas: ")
    for x in palabrasUsadas:
        print("%s\n%s\n" % (x, palabrasUsadas[x]))

def imprimirLetras():
    print("Guía de Coincidencias:\n• =: Coincide\n• -: Se encuentra\n• ~: No está\n\nLetras Usadas: ")
    i = 0
    for x in letras:
        print("%s: %s" % (x, letras[x]))
        i += 1
    print()

def añadirPalabras(palabra):
    with open("posiblesPalabras%iletras.txt" % (cantidadLetras), "a+") as archivo:
        archivo.write(palabra + '\n')
        palabras.append(palabra.strip())

def pasarSegundosAHorasMinutosSegundos(segundos):
    segundos = int(segundos)
    minutos = 0
    horas = 0
    while segundos >= 60:
        segundos -= 60
        minutos += 1
    while minutos >= 60:
        minutos -= 60
        horas += 1
    tiempo = [horas, minutos, segundos]
    return tiempo

def mostrarResultados(jug):
    porcentajeVictorias = (estadisticasJugador[jug]['aciertos']/(estadisticasJugador[jug]['partidas']))*100
    print("Jugador: %s\
           \nEstadísticas:\
           \nJugadas: %i | Victorias: %d (Porcentaje) | Racha Actual: %i | Mejor Racha: %i"
           % (jugadores[jug], estadisticasJugador[jug]['partidas'], porcentajeVictorias, estadisticasJugador[jug]['racha'], estadisticasJugador[jug]['mejorRacha']))
    print("Distribución:")
    i = 1
    while i <= cantidadIntentos:
        print("%i: %i" % (i, estadisticasJugador[jug][i.__str__()]))
        i += 1
    print("Fallos: %i\
          \nTiempo: %02i:%02i:%02i" % (estadisticasJugador[jug]['fallos'], estadisticasJugador[jug]['tiempo'][0], estadisticasJugador[jug]['tiempo'][1], estadisticasJugador[jug]['tiempo'][2]))

def registrarEstadisticas(jug):
    with open("registroEstadisticas.txt", "a+") as archivo:
        archivo.write("Jugador: %s\n" % (jugadores[jug]))
        porcentajeVictorias = (estadisticasJugador[jug]['aciertos']/(estadisticasJugador[jug]['partidas']))*100
        archivo.write("Estadisticas:\n")
        archivo.write("Jugadas: %i | Victorias: %d (Porcentaje) | Racha Actual: %i | Mejor Racha: %i"
        % (estadisticasJugador[jug]['partidas'], porcentajeVictorias, estadisticasJugador[jug]['racha'], estadisticasJugador[jug]['mejorRacha']))
        archivo.write("\nDistribucion:\n")
        i = 1
        while i <= cantidadIntentos:
            archivo.write("%i: %i\n" % (i, estadisticasJugador[jug][i.__str__()]))
            i += 1
        archivo.write("Fallos: %i\n" % (estadisticasJugador[jug]['fallos']))
        archivo.write("Tiempo: %02i:%02i:%02i\n" % (estadisticasJugador[jug]['tiempo'][0], estadisticasJugador[jug]['tiempo'][1], estadisticasJugador[jug]['tiempo'][2]))
        archivo.write('\n')

def cambiarTurno(turno):
    if turno == 0:
        turno = 1
    elif turno == 1:
        turno = 0
    return turno

def vaciarListaLetras():
    for x in letras:
        letras[x] = ''

setDificultad()

cantidadJugadores = int(input("Modo de juego:\n[1] 1 Jugador\n[2] 2 Jugadores\n"))
while cantidadJugadores != 1 and cantidadJugadores != 2:
    cantidadJugadores = int(input("Valor inválido. Debe responder con 1 o 2.\nModo de juego:\n[1] 1 Jugador\n[2] 2 Jugadores\n"))

if cantidadJugadores == 1:
    jugadores = [input("Nombre Jugador: ")]
else:
    jugadores = [input("Nombre Jugador 1: "), input("Nombre Jugador 2: ")]

turno = 0

comienzo = time.time()
while terminar == False:
    palabra = palabras[random.randrange(0, len(palabras))]
    estadisticasJugador[turno]['partidas'] += 1
    intento = 1
    while intento <= cantidadIntentos:
        os.system('cls')
        if intento > 1:
            imprimirPalabrasUsadas()
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
            acertar(turno)
            intento = 999
        elif intento == cantidadIntentos:
            fallar(turno)
        elif intento < cantidadIntentos:
            palabrasUsadas[palabraConEspacios] = coincidencias
        
        intento += 1
        print()
    
    estadisticasJugador[0]['fin'] = time.time()
    estadisticasJugador[1]['fin'] = time.time()
    estadisticasJugador[turno]['tiempo'] = pasarSegundosAHorasMinutosSegundos(estadisticasJugador[turno]['fin'] - comienzo)
    palabrasUsadas.clear()
    
    mostrarResultados(turno)
    
    for x in palabrasNoEncontradas:
        respuesta = input("¿Le gustaría añadir la palabra %s a la lista de posibles palabras? (s = sí): " % (x)).lower()
        if respuesta == 's':
            añadirPalabras(x)
        else:
            print("La palabra %s no se ha añadido a la lista de posibles palabras." % (x))

    vaciarListaLetras()
    palabrasNoEncontradas.clear()
    
    turno = cambiarTurno(turno)
    if input("¿Desea continuar jugando? (s = sí): ").lower() != 's':
            terminar = True
            
            registrarEstadisticas(0)
            if cantidadJugadores == 2:
                registrarEstadisticas(1)
