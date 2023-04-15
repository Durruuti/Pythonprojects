#Definir las funciones necesitadas, add, sub, mul, div
#Printear las opciones al usuario
#Preguntar por valores
#Llamar a las funciones
#Loop while para que el programa continue hasta que lo indique

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print(str(a) + " /" + str(b) + " = " + str(answer) + "\n")

while True:
    print("A. Suma")
    print("B. Resta")
    print("C. Multiplicación")
    print("D. División")
    print("E. Salir")

    choice = input("Introduce la opción [LETRA] : ")

    if choice == "a" or choice == "A":
        print("Suma")
        a = int(input("Introduce el primer numero: "))
        b = int(input("Introduce el segundo numero: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Resta")
        a = int(input("Introduce el primer numero: "))
        b = int(input("Introduce el segundo numero: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplicación")
        a = int(input("Introduce el primer numero: "))
        b = int(input("Introduce el segundo numero: "))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("División")
        a = int(input("Introduce el primer numero: "))
        b = int(input("Introduce el segundo numero: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("El programa ha finalizado")
        quit()
