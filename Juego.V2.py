import random

def juego_de_sumas():
    print(" bienvenido al Juego de sumas")
    preguntas_totales = 5
    puntaje = 0
    
    for i in range(1, preguntas_totales + 1):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        resultado_correcto = num1 + num2
        
        print(f"Pregunta {i}: ¿Cuánto es {num1} + {num2}?")
        try:
            respuesta_usuario = int(input("Tu respuesta: "))
        except ValueError:
            print("Por favor, solo números.")
            respuesta_usuario = None

        if respuesta_usuario == resultado_correcto:
            print("correcto 🎉\n")
            puntaje += 1
        else:
            print(f"incorrecto. el resultado correcto era {resultado_correcto}. \n")
            
    print("--- Juego Terminado ---")
    print(f"tu puntaje final es: {puntaje} de {preguntas_totales}")


turno = 0

while turno != 1:

    juego_de_sumas()

    respuesta = input("Queres volver a jugar? si/no: ")

    if respuesta == "si":

        print("Otra oportunidad")
    

    else:
        print("Nos vemos")
        turno = 1