# OC P7 - GrandPyBot
## 1. Présentation

GrandPyBot est une application permettant de trouver une adresse et éventuellement des informations à partir d'une requête.  

---
## 2. Fonctionnalités
Plusieurs fonctionnalités sont nécessaires pour la réalisation de ce projet:

- Parsing des requêtes
- Appel de l'API Google Maps et Wikipedia
- Réponse AJAX
- Affichage du résultat sur une carte

---
## 3. Pré-requis
Python >= 3.8  
Clés d'API Google Maps  
Les clés d'API nécessaires peuvent êtes obtenues sur le site de [Google Maps Platform](https://cloud.google.com/maps-platform/)  
2 clés sont nécessaires :
- Clé restreinte à `Places API`
- Clé restreinte à `Maps JavaScript API`
    - Cette clé sera publique, elle doit donc aussi être restreinte au référent HTTP correspondant à l'URL de l'application

Ces clés doivent respectivement être placées dans les variables d'environnement sous les noms suivants:
- `MAPS_KEY`
- `MAPS_JS_KEY`

---
## 4. Utilisation

### Debug
Pour lancer l'application en debug, il suffit de:
- Créer un environnement virtuel: `python -m venv venv`
- Activer cet environnement virtuel:
    - Windows : .\venv\Scripts\Activate.ps1
    - Linux / Mac : source venv/bin/activate
- Installer les dépendances: `pip install -r requirements.txt`
- Créer un fichier `keys.py` à la racine, avec les clés d'API en suivant l'exemple du fichier `keys.py.sample`
- Lancer l'application: `python run.py`

### Production
Pour lancer l'application en production sur Heroku, il suffit de:
- Créer une application sur Heroku
- Ajouter les clés d'API nécessaires dans les `Config Vars`
- Forker/cloner le dépôt GitHub
- Lier l'application Heroku au dépôt Github créé
- Activer le déploiement automatique

