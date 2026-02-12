import sys
import os
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap

# crea una carpeta llamada imágenes y guarda tus archivos

# función principal: 

def mostrar_imagen_y_mensaje(label_img, label_msg, carpeta="imagenes"):
    archivos = os.listdir(carpeta)
    imagenes = [f for f in archivos if f.endswith((".png", ".jpg", ".jpeg"))]
    mensajes = [
        # agrega aquí los mensajes que quieras
    ]
    if imagenes:
        seleccion = random.choice(imagenes)
        ruta = os.path.join(carpeta, seleccion)
        pixmap = QPixmap(ruta)
        label_img.setPixmap(pixmap.scaled(400, 400))  # Ajusta tamaño
        label_msg.setText(random.choice(mensajes))

def iniciar_app():
    app = QApplication(sys.argv)
    ventana = QWidget()
    ventana.setWindowTitle("Galería Aleatoria con Mensajes")

    layout = QVBoxLayout()

    etiqueta_img = QLabel("tu texto")
    layout.addWidget(etiqueta_img)

    etiqueta_msg = QLabel("tu texto")
    # agrega el widget al layout

    boton = QPushButton("tu texto")
    # agrega el widget al layout

    def on_click():
        # define qué hará el programa cuando presiones el botón
        # pista: ya definiste una función para eso

    # la función no hará nada hasta que definas on_click()
    #boton.clicked.connect(on_click)

    ventana.setLayout(layout)
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    iniciar_app()