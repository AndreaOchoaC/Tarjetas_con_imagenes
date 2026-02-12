import sys
import os
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw, ImageFont

def mostrar_imagen_con_texto(label_img, carpeta="imagenes"):
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
        
        # Abrir imagen con PIL
        img = Image.open(ruta).convert("RGBA")
        draw = ImageDraw.Draw(img)
        
        # Fuente (puedes usar otra ruta si quieres una fuente especial)
        try:
            font = ImageFont.truetype("arial.ttf", 30)
        except:
            font = ImageFont.load_default()
        
        mensaje = random.choice(mensajes)
        
        # Calcular tamaño del texto (compatibilidad con Pillow <10 y >=10)
        try:
            text_w, text_h = font.getsize(mensaje)
        except AttributeError:
            bbox = draw.textbbox((0,0), mensaje, font=font)
            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]
        
        w, h = img.size
        pos = ((w - text_w) // 2, h - text_h - 20)  # centrado abajo
        
        # Dibujar texto con sombra
        draw.text((pos[0]+2, pos[1]+2), mensaje, font=font, fill="black")
        draw.text(pos, mensaje, font=font, fill="white")
        
        # Guardar imagen temporal
        salida = "temp.png"
        img.save(salida)
        
        # Mostrar en PyQt
        pixmap = QPixmap(salida)
        label_img.setPixmap(pixmap.scaled(400, 400))

def iniciar_app():
    app = QApplication(sys.argv)
    ventana = QWidget()
    ventana.setWindowTitle("Galería Aleatoria con Mensajes en la Imagen")

    layout = QVBoxLayout()

    etiqueta_img = QLabel("Aquí aparecerá la imagen con mensaje")
    layout.addWidget(etiqueta_img)

    boton = QPushButton("Mostrar imagen con mensaje")
    layout.addWidget(boton)

    def on_click():
        mostrar_imagen_con_texto(etiqueta_img)

    boton.clicked.connect(on_click)

    ventana.setLayout(layout)
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    iniciar_app()