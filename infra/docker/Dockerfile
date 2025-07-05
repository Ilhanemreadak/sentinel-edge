# infra/docker/Dockerfile
FROM python:3.11-slim

WORKDIR /code

# Daha küçük katmanlar için requirements ayrı kopyalanır
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Uygulama dosyaları
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
