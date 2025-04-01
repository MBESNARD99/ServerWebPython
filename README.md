# ServerWebPython
Projet universitaire dans le but de se familiariser avec le fait de créer un serveur web via python

## Description

Ce projet a été réalisé dans le cadre d'un cours universitaire afin d'apprendre les bases de la création et de la gestion d'un serveur web en utilisant le langage Python.

## Prérequis

- Python 3.x
- Bibliothèques Python nécessaires (voir `requirements.txt` si disponible)

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/MBESNARD99/ServerWebPython.git
   ```

2. Accédez au répertoire du projet :

   ```bash
   cd ServerWebPython
   ```

3. (Optionnel) Créez un environnement virtuel :

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sur macOS/Linux
   venv\Scripts\activate     # Sur Windows
   ```

4. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

Lancez le serveur avec la commande suivante :

```bash
python app.py
```

Accédez ensuite au serveur via votre navigateur à l'adresse `http://localhost:5000`.

## Structure du projet

- `app.py` : Script principal pour démarrer le serveur.
- `templates/` : Dossier contenant les fichiers HTML pour le rendu des pages.
- `static/` : Dossier pour les fichiers statiques (CSS, JavaScript, images).

## Contribuer

Les contributions sont les bienvenues. Pour proposer des modifications, veuillez créer une branche dédiée, apporter vos modifications et soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
