# Librerias requeridas
# Crear una funcion que recolecte el texto y lo convierta en qr
# guardar el qr comouna imagen
# arrancar la funcion

import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qring.png")


url = input("Introduzca la url: ")
generate_qrcode(url)
