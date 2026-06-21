import random

def juego_de_sumas():
    print(" ¡Bienvenido al Juego de sumar! ")
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
            print("Por favor, ingresa solo números.")
            respuesta_usuario = None

        if respuesta_usuario == resultado_correcto:
            print("¡Correcto! ¡Buen trabajo! 🎉\n")
            puntaje += 1
        else:
            print(f"Incorrecto. El resultado correcto era {resultado_correcto}. 💡\n")
            
    print("--- Juego Terminado ---")
    print(f"Tu puntaje final es: {puntaje} de {preguntas_totales}")

juego_de_sumas()
