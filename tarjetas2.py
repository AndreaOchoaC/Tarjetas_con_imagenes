import sys
import os
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap

def mostrar_imagen_y_mensaje(label_img, label_msg, carpeta="imagenes"):
    archivos = os.listdir(carpeta)
    imagenes = [f for f in archivos if f.endswith((".png", ".jpg", ".jpeg"))]
    mensajes = [
        "¡Feliz día!",
        "Te invito a invitarme unos chocolates",
        "Soy talla \"un auto último modelo\" ",
        "Feliz San Valentín 🌹",
        "✨✨✨"
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

    etiqueta_img = QLabel("Aquí aparecerá la imagen")
    layout.addWidget(etiqueta_img)

    etiqueta_msg = QLabel("Aquí aparecerá el mensaje")
    layout.addWidget(etiqueta_msg)

    boton = QPushButton("Mostrar imagen y mensaje")
    layout.addWidget(boton)

    def on_click():
        mostrar_imagen_y_mensaje(etiqueta_img, etiqueta_msg)

    boton.clicked.connect(on_click)

    ventana.setLayout(layout)
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    iniciar_app()