# Basis: schlankes Python-Image
FROM python:3.11-slim

# Arbeitsverzeichnis
WORKDIR /app

# System-Dependencies (falls nötig)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Requirements kopieren & installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code und statische Dateien kopieren
COPY server.py .
COPY static/ static/

# Port freigeben
EXPOSE 8080

# Startbefehl
CMD ["python", "server.py"]
