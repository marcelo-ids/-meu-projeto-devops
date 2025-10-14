# app.py
from flask import Flask, send_file
from draw_star_pillow import create_star_with_pillow

# Primeiro, gera a imagem da estrela UMA ÚNICA VEZ quando o app inicia
create_star_with_pillow()

app = Flask(__name__)

@app.route('/')
def home():
    # Agora, a rota apenas envia o arquivo que já foi criado
    return send_file('static/star.png', mimetype='image/png')
