# draw_star_pillow.py
from PIL import Image, ImageDraw
import os

def create_star_with_pillow():
    # Garante que a pasta 'static' exista
    if not os.path.exists('static'):
        os.makedirs('static')

    # Cria uma imagem preta, 400x400 pixels
    img = Image.new('RGB', (400, 400), 'black')
    draw = ImageDraw.Draw(img)

    # Define as coordenadas dos 5 pontos da estrela
    # (Não se preocupe com a matemática, são só os pontos no plano cartesiano)
    points = [
        (200, 50), (239, 159), (359, 159), (269, 231),
        (299, 341), (200, 270), (101, 341), (131, 231),
        (41, 159), (161, 159)
    ]

    # Desenha o polígono da estrela com contorno amarelo e preenchimento dourado
    draw.polygon(points, outline='yellow', fill='gold')

    # Salva a imagem
    img.save('static/star.png')
    print("Estrela gerada com sucesso usando Pillow!")
