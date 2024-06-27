# Utilisez une image de base légère de Python
FROM python:3.8-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel l'application va s'exécuter
EXPOSE 5000

# Définir la commande pour démarrer l'application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
