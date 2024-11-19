# AXA Project

 data.csv a use it for this endpoint '/upload-csv/'

http://localhost:5000/apidocs

## Introduction
Ce projet comprend les parties frontend et backend. Ce document explique comment utiliser Docker Compose pour démarrer le projet.

## Prérequis
- Docker
- Docker Compose

## Structure du projet
- `frontend/` : Contient le code source de l'application frontend.
- `backend/` : Contient le code source de l'application backend.
- `docker-compose.yml` : Fichier de configuration pour Docker Compose.

## Instructions

### 1. Cloner le dépôt
```bash
git clone https://github.com/votre-utilisateur/axa-project.git
cd axa-project
```

### 2. Construire et démarrer les conteneurs
```bash
docker-compose up --build
```

### 3. Accéder aux applications
- Frontend : [http://localhost:3000](http://localhost:3000)
- Backend : [http://localhost:8000](http://localhost:8000)

### 4. Arrêter les conteneurs
```bash
docker-compose down
```

## Fichiers importants
- `docker-compose.yml` : Définit les services, réseaux et volumes pour Docker.
- `Dockerfile` (dans `frontend/` et `backend/`) : Instructions pour construire les images Docker.


