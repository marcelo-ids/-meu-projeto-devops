# draw_star.py
import turtle
from PIL import Image
import io

def create_star_image():
    # Configura a tela do Turtle em memória, sem abrir janela
    screen = turtle.Screen()
    screen.setup(400, 400)
    screen.tracer(0) # Desliga as animações para ser mais rápido

    # Cria a tartaruga
    star_turtle = turtle.Turtle()
    star_turtle.hideturtle()
    star_turtle.color("yellow", "gold")
    
    # Desenha a estrela
    star_turtle.begin_fill()
    for _ in range(5):
        star_turtle.forward(100)
        star_turtle.right(144)
    star_turtle.end_fill()

    # Atualiza a tela para garantir que o desenho apareça
    screen.update()

    # Salva o desenho como um arquivo PostScript em memória
    ps_io = io.BytesIO()
    canvas = screen.getcanvas()
    canvas.postscript(file=ps_io, colormode='color')

    # Usa a biblioteca Pillow para converter o PostScript para PNG
    ps_io.seek(0)
    img = Image.open(ps_io)
    
    # Salva a imagem final em uma pasta 'static'
    # O Flask usa essa pasta por padrão para servir arquivos como imagens, CSS, etc.
    img.save("static/star.png", "png")
    
    # Limpa a tela para a próxima vez
    screen.clear()
