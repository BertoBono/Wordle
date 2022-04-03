import random

palabras = []
palabrasNoEncontradas = []
respuesta = 's'
puntajes = {
    'partidas': 0, 'racha': 0, 'mejorRacha': 0,
    'aciertos': 0,
    '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0,
    'fallos': 0
}

with open("posiblesPalabras.txt", "r") as archivo:
    for x in archivo:
        palabras.append(x.strip())

def mostrarResultados():
    porcentajeVictorias = (puntajes['aciertos']/(puntajes['partidas']))*100
    print("\
        \nEstadísticas:\
            \nJugadas: %i | Victorias: %d (Porcentaje) | Racha Actual: %i | Mejor Racha: %i\
        \nDistribución:\
            \nIntento 1:\t%i\nIntento 2:\t%i\nIntento 3:\t%i\nIntento 4:\t%i\nIntento 5:\t%i\nIntento 6:\t%i\nFallos:\t\t%i"\
        % (puntajes['partidas'], porcentajeVictorias, puntajes['racha'], puntajes['mejorRacha'],\
        puntajes['1'], puntajes['2'], puntajes['3'], puntajes['4'], puntajes['5'], puntajes['6'], puntajes['fallos']))

def compararPalabras(ingreso):
    i = 0
    coincidencias = ''
    for x in ingreso:
        if x == palabra[i]:
            coincidencias += '='
        elif x in palabra:
            coincidencias += '-'
        else:
            coincidencias += ' '
        i += 1
    return coincidencias

def imprimirConEspacios(palabra):
    for x in palabra:
        print(x, end=' ')

def acertar():
    print("\nACERTASTE!!!")
    puntajes['aciertos'] += 1
    puntajes[intentos.__str__()] += 1
    if puntajes['mejorRacha'] == puntajes['racha']:
        puntajes['mejorRacha'] += 1
    puntajes['racha'] += 1

def fallar():
    print("\nFALLASTE!!!")
    print("La palabra era %s" % (palabra))
    puntajes['fallos'] += 1
    puntajes['racha'] = 0

def añadirPalabras(palabra):
    with open("posiblesPalabras.txt", "a+") as archivo:
        archivo.write(palabra + '\n')
        palabras.append(palabra.strip())        
        
while respuesta == 's':
    palabra = palabras[random.randrange(0, len(palabras))]
    puntajes['partidas'] += 1
    intentos = 1
    while intentos <= 6:
        ingreso = ''
        print()
        while ingreso not in palabras:
            palabrasNoEncontradas.append(ingreso)
            ingreso = input("Ingrese una palabra de 5 letras: ").upper()
            if ingreso not in palabras:
                print("Esa palabra no se encuentra entre las posibles palabras.")
        ingreso = ingreso.upper()

        imprimirConEspacios(ingreso)
        print()
        imprimirConEspacios(compararPalabras(ingreso))
        
        if ingreso == palabra:
            acertar()
            intentos = 999
        elif intentos == 6:
            fallar()
        intentos += 1
    
    mostrarResultados()
    print()
    for x in palabrasNoEncontradas:
            if x not in palabras and len(x) == 5:
                respuesta = ''
                while respuesta != 's' and respuesta != 'n':
                    respuesta = input("¿Le gustaría añadir la palabra %s a la lista de posibles palabras? (s = sí/n = no): " % (x))
                    if respuesta == 's':
                        añadirPalabras(x)
                    elif respuesta == 'n':
                        print("La palabra %s no se ha añadido a la lista de posibles palabras." % (x))
                        palabrasNoEncontradas.remove(x)
    
    respuesta = ''
    print()
    while respuesta != 's' and respuesta != 'n':
        respuesta = input("¿Seguir jugando? (s = sí/n = no): ")
