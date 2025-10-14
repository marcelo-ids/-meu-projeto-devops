# Dockerfile

# 1. Imagem base super leve
FROM python:3.9-slim

# 2. Diretório de trabalho
WORKDIR /app

# 3. Copia e instala as poucas dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia o resto do código
COPY . .

# 5. Expõe a porta 5000
EXPOSE 5000

# 6. Comando simples para iniciar o app
CMD ["flask", "run", "--host=0.0.0.0"]
