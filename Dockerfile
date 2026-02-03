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
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libpango-1.0-0 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libexpat1 \
    libfontconfig1 \
    libgcc1 \
    libglib2.0-0 \
    libnspr4 \
    libpangocairo-1.0-0 \
    libstdc++6 \
    libx11-6 \
    libx11-xcb1 \
    libxcb1 \
    libxcursor1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxrender1 \
    libxtst6 \
    fonts-liberation \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Instala o Google Chrome e ChromeDriver
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Obtem a versao do Chrome e instala o ChromeDriver correspondente
RUN CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+' | head -1) && \
    CHROME_MAJOR=$(echo $CHROME_VERSION | cut -d. -f1) && \
    echo "Chrome version: $CHROME_VERSION (major: $CHROME_MAJOR)" && \
    # Para Chrome 115+, usa o novo endpoint de download
    CHROMEDRIVER_URL="https://storage.googleapis.com/chrome-for-testing-public/$(curl -s https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_$CHROME_MAJOR)/linux64/chromedriver-linux64.zip" && \
    echo "Downloading ChromeDriver from: $CHROMEDRIVER_URL" && \
    wget -q -O /tmp/chromedriver.zip "$CHROMEDRIVER_URL" && \
    unzip /tmp/chromedriver.zip -d /tmp/ && \
    mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver* && \
    chromedriver --version

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
