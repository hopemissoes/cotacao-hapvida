# Dockerfile para Cotacao Hapvida
FROM python:3.11-slim

# Instala Chromium e ChromeDriver do repositorio (mais estavel no Docker)
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    wget \
    gnupg \
    unzip \
    curl \
    xvfb \
    libnss3 \
    libxss1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libdrm2 \
    libgbm1 \
    libxkbcommon0 \
    fonts-liberation \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Verifica instalacao do Chromium e ChromeDriver
RUN echo "=== Verificando instalacao ===" && \
    which chromium && \
    chromium --version && \
    which chromedriver && \
    chromedriver --version && \
    echo "=== Instalacao OK ==="

# Define diretorio de trabalho
WORKDIR /app

# Copia requirements e instala dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o codigo da aplicacao
COPY app_cotacao.py .
COPY templates/ templates/

# Expoe a porta
EXPOSE 5000

# Variaveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV DISPLAY=:99
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Comando para iniciar a aplicacao
CMD ["python", "app_cotacao.py"]
