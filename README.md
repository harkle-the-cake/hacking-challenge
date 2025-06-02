# Hack-Challenge
Repo um Hack-Challenges für Azubis bereitzustellen.

## 🔒 Sicherheitshinweis
Diese Projekte sind nur für Lern- und Übungszwecke gedacht und enthält absichtlich Schwachstellen wie hartcodierte Passwörter. Nicht produktiv einsetzen.

## Hack-Challenge 2025

Diese kleine Hacking-Challenge richtet sich an IT-Azubis und läuft auf einem Raspberry Pi, öffentlich erreichbar unter:

📍 **https://hack.boxwork.eu/2025/**

### 🔍 Aufgabe
Finde das im JavaScript versteckte Passwort und sende es per POST an `/2025/code`. Wenn das Passwort korrekt ist, bekommst du einen persönlichen Code mit Zeitstempel.

### ✅ Verifizieren
Gib den erhaltenen Code + Zeitstempel bei `/2025/verify` ein. Wenn alles passt, bekommst du als Belohnung einen Energy-Drink.

### 📂 Projektstruktur
hack-challenge/2025/
├── static/
│ └── index.html
├── server.py
├── requirements.txt
└── README.md

### 🛠️ Starten (lokal)
```bash
pip install -r requirements.txt
python server.py
```

### 🐳 Docker-Setup (empfohlen)

#### 🧱 Voraussetzungen (für Debian/Raspberry Pi)

```bash
sudo apt-get update
sudo apt-get install -y \
    docker.io \
    docker-compose \
    git
sudo systemctl enable docker
sudo usermod -aG docker $USER
```
⚠️ Anschließend: aus- und wieder einloggen, damit die Gruppe docker aktiv wird.


### 🐳 Starten
git clone https://github.com/dein-benutzername/hack-challenge.git
cd hack-challenge/2025
docker-compose up --build -d
