# Proyecto -- crear tarjetas con PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QListWidget
import turtle

def dibujar_tarjeta(mensaje):
    t = turtle.Turtle()
    t.color("red", "pink")
    t.begin_fill()
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
    t.end_fill()

    t.penup()
    t.goto(0, -20)
    t.color("black")
    t.write(mensaje, align="center", font=("Arial", 16, "bold"))
    turtle.done()

def mostrar_opciones():
    app = QApplication(sys.argv)
    ventana = QWidget()
    ventana.setWindowTitle("Elige tu mensaje de San Valentín")

    layout = QVBoxLayout()

    etiqueta = QLabel("Selecciona un mensaje:")
    layout.addWidget(etiqueta)

    lista = QListWidget()
    mensajes = ["Te quiero 💖", "Eres mi universo 🌌", "Feliz San Valentín 🌹", "Siempre juntos 💕"]
    lista.addItems(mensajes)
    layout.addWidget(lista)

    boton = QPushButton("Crear tarjeta")
    layout.addWidget(boton)

    def on_click():
        mensaje = lista.currentItem().text()
        ventana.close()
        dibujar_tarjeta(mensaje)

    boton.clicked.connect(on_click)

    ventana.setLayout(layout)
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    mostrar_opciones()