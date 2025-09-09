FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# системные зависимости для Chromium + Xvfb
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libcairo2 \
    libasound2 \
    fonts-liberation \
    libwoff1 \
    libharfbuzz0b \
    libxshmfence1 \
    xdg-utils \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code/encar_parse

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# создаем пользователя и рабочие папки
RUN adduser --disabled-password --gecos '' celeryuser && \
    mkdir -p /code/staticfiles /code/media && \
    chown -R celeryuser:celeryuser /code/encar_parse

USER celeryuser

# браузеры Playwright под пользовательский $HOME
RUN playwright install chromium

COPY . .

# обертка для запуска с виртуальным дисплеем
ENTRYPOINT ["xvfb-run", "--server-args=-screen 0 1920x1080x24", "python"]
