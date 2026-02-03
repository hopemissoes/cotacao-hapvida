# Dockerfile para Cotacao Hapvida
FROM python:3.11-slim

# Instala dependencias do sistema para Chrome/Selenium
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    libnss3 \
    libxss1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libdrm2 \
    libgbm1 \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

# Instala o Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

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

# Comando para iniciar a aplicacao
CMD ["python", "app_cotacao.py"]
