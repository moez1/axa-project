# Utiliser une image de base officielle de Node.js
FROM node:14

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY . /app

# Installer les dépendances
RUN npm install

# Construire l'application
RUN npm run build

# Exposer le port sur lequel l'application s'exécute
EXPOSE 3000

# Définir la commande pour exécuter l'application
CMD ["npm", "start"]