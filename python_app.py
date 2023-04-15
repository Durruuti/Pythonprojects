# diccionario que guarde preguntas y respuestas
# tener una variable que registre la puntuacion del jugador
#Hacer unn bucle a través de un diccionario utilizando valores clave
#Mostrar cada cuestión
# Mostrar si acierta o falla
# Mostrar el resultado cuando el quiz acabe

quiz = {
    "question1": {
        "question": "Cual es la capital de Francia",
        "answer": "Paris"
    },
    "question2": {
        "question": "Cual es la capital de Alemania",
        "answer": "Berlín"
    },
    "question3": {
        "question": "Cual es la capital de Italia",
        "answer": "Roma"
    },
    "question4": {
        "question": "Cual es la capital de España",
        "answer": "Madrid"
    },
    "question5": {
        "question": "Cual es la capital de Portugal",
        "answer": "Lisboa"
    },
    "question6": {
        "question": "Cual es la capital de Suiza",
        "answer": "Berna"
    },
    "question7": {
        "question": "Cual es la capital de Austria",
        "answer": "Viena"
    },
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Respuesta? :")

    if answer.lower() == value["answer"].lower():
        print("Correcto")
        score += 1
        print("Tu score es: " + str(score))
    else:
        print("Maaal!")
        print("La respuesta es: " + value["answer"])
        print("Tu score es: " + str(score))
        print("")
        print("")

print("Tienes: " + str(score) + "de 7 respuestas correctas!")
print("Tu porcentaje de acierto es: " + str(int(score/7 * 100)) + "%")

