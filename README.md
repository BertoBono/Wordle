# GRUPO 1:

# INSTRUCCIONES: 
* La carpeta que contenga el archivo 'wordle.py' debe contener los siguientes archivos:
  * 'posiblesPalabras5letras.txt'
  * 'posiblesPalabras6letras.txt'
  * 'posiblesPalabras7letras.txt'
  * 'posiblesPalabras8letras.txt'
  * 'registroEstadisticas.txt'

* No es necesario disponer de una conexión a internet

* Cómo usar el programa:
  * Al ejecutar wordle.py:
1. Ingresar la cantidad de letras para las posibles palabras que se puedan usar (el valor debe ser un número entero entre 5 y 8 inclusive)
2. Ingresar la cantidad de intentos para poder adivinar la palabra (el valor debe ser un número entero entre 3 y 9 inclusive)
3. Se pide una confirmación para las dos anteriores opciones (la cantidad de letras o de intentos no puede ser cambiada durante la ejecución del programa si se            responde que 's')
4. Ingresar la cantidad de jugadores (1 o 2)
5. Ingresar el nombre de el/los jugador/es
6. Entonces ya comienza un bucle para comenzar a intentar adivinar las palabras
    * Las palabras ingresadas solo se tendran en cuenta como intentos, si se encuentran entre la lista de 'posiblesPalabras_N_letras.txt' (N = cantidad de letras                 seleccionada)
    * Cuando una palabra con N cantidad de letras es ingresada, si no se encuentra en 'posiblesPalabras_N_letras.txt' (N = cantidad de letras seleccionada) se agrega a         una lista de palabras. Al finalizar ese intento, se le pregunta al usuario si quiere que esa palabra sea ingresada a la 'posiblesPalabras_N_letras.txt' (N =             cantidad de letras seleccionada). Si la palabra no tiene N cantidad de letras, entonces no va a ser tenida en cuenta para este punto.
    * Si se logra adivinar la palabra antes de que se acaben los turnos, se le agregara un 'acierto', su 'racha' aumenta en 1 punto y se especificará en que turno             encontró la respuesta, en las estadisticas de ese jugador. 
    * Si no se logra adivinar la palabra antes de que se acaben los turnos, se le agregara un 'fallo', su 'racha' vuelve a 0.
    * Si la 'racha' del jugador supera a su propia 'mejorRacha' entonces a 'mejorRacha' va a aumentar hasta que se consiga un fallo.
    * El tiempo del jugador es el total de tiempo desde que empezó a adivinar (Solo se tiene en cuenta el tiempo mientras se intenta adivinar).
    * Al finalizar el programa, respondiendo algo que no sea 's' a la pregunta de "¿Desea continuar jugando?", las estadisticas de el/los jugador/es se registran en           'registroEstadisticas.txt'.
    * Cada vez que se intente adivinar una palabra, se imprime en pantalla una lista de las palabras que ya se intentaron, y una lista de letras, para que el usuario           pueda comprobar que palabras y letras ya intentó usar, y que resultado le dio.

# INTEGRANTES:
* Lucas Bertoli
* Bautista Della Penna
* Bono Neer
* Fernando Torre
