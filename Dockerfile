FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Установка make и других полезных инструментов
RUN apt-get update && \
    apt-get install -y make git curl && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install -e .

CMD ["bash"]