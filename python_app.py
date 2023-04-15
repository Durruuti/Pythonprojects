#Recoger el email del usuario
#Dvidir el email usando @, la primera arte como el usuario, la segunda parte como dominio
#Dividir el dominio utilizando .,

def main():
    print("Benvenido a email slicer")
    print("")

    email_input = input("Introduce tu email: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Usuario :", username)
    print("Dominio :", domain)
    print("Extensón :", extension)

main()