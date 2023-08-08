# Image de base
FROM python:3.11

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers de l'application
COPY . /app

# Installation des dépendances
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Exposition du port
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["uvicorn", "application.mpeak_api:app", "--host", "0.0.0.0", "--port", "8000"]
