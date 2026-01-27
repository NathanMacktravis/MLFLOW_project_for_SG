# MLFLOW_project_for_SG

## Description du projet

Ce projet vise à développer un pipeline de **classification des maladies rénales à partir d’images médicales** à l’aide d’un modèle de Deep Learning. Il illustre les bonnes pratiques **MLOps** en combinant **DVC** pour le versionnement des données et des pipelines, **MLflow** pour le suivi et la traçabilité des expériences, ainsi que **Flask** pour le déploiement du modèle sous forme d’API.  

Le projet couvre l’ensemble du cycle de vie d’un modèle de Machine Learning/Deep Learning classique : ingestion des données, entraînement, évaluation et mise à disposition via une application. Il n’est pas entièrement finalisé, car le déploiement **CI/CD avec Docker sur AWS** n’a pas été implémenté, principalement par manque de temps 😆

---

## Workflow de travail

1. Mettre à jour le fichier `config.yaml`
2. Mettre à jour le fichier `secrets.yaml` (optionnel)
3. Mettre à jour le fichier `params.yaml`
4. Mettre à jour les entités
5. Mettre à jour le gestionnaire de configuration dans le dossier `src/config`
6. Mettre à jour les composants
7. Mettre à jour le pipeline
8. Mettre à jour le fichier `main.py`
9. Mettre à jour le fichier `dvc.yaml`
10. Mettre à jour le fichier `app.py`

---

## Comment exécuter le projet ?

### Étapes :

Cloner le dépôt

```bash
https://github.com/NathanMacktravis/MLFLOW_project_for_SG
```

### ÉTAPE 01 – Créer un environnement conda après avoir ouvert le dépôt

```bash
conda create -n .env python=3.12 -y
```

```bash
conda activate .env
```

---

### ÉTAPE 02 – Installer les dépendances

```bash
pip install -r requirements.txt
```

```bash
# Enfin, exécuter la commande suivante
python app.py
```

Ensuite,

```bash
ouvrir le localhost et le port affiché
```

---

## MLflow

* [Documentation officielle](https://mlflow.org/docs/latest/index.html)

##### Commande

* `mlflow ui`

---

### Dagshub

Plateforme permettant d’héberger MLflow et de centraliser le suivi des expériences.

[Dagshub](https://dagshub.com/)

Les variables suivantes sont utilisées pour configurer MLflow avec Dagshub :

```bash
MLFLOW_TRACKING_URI=TRACKING_URI
MLFLOW_TRACKING_USERNAME= USERNAME
MLFLOW_TRACKING_PASSWORD=TOKEN
python script.py
```

Exécuter les commandes suivantes pour exporter les variables d’environnement :

```bash
export MLFLOW_TRACKING_URI=TRACKING_URI

export MLFLOW_TRACKING_USERNAME=USERNAME

export MLFLOW_TRACKING_PASSWORD=TOKEN
```

---

## Commandes DVC

1. Initialiser DVC dans le projet
2. Reproduire le pipeline
3. Visualiser le graphe du pipeline

```bash
dvc init
dvc repro
dvc dag
```

---

## À propos de MLflow et DVC

### MLflow

* Outil prêt pour la production
* Permet de tracer toutes les expériences
* Gère le logging et le tagging des modèles

### DVC

* Outil léger, adapté aux POC
* Permet de suivre les expériences de manière simple
* Permet l’orchestration des pipelines (création de pipelines ML)

---