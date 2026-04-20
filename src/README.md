# ProjetRST

## 📁 Dossier `src/`

Le dossier `src/` contient l’ensemble du code source de **ProjetRST**.  
Il suit une architecture modulaire, claire et extensible, permettant une évolution
progressive du projet sans dette technique.

---


---

### 🎯 Objectifs du dossier

- Centraliser tout le code Python du projet  
- Fournir une architecture propre et maintenable  
- Séparer clairement les responsabilités (client, API, modules, configuration)  
- Faciliter les tests unitaires et l’extension du projet  

---

### 🧩 Composants principaux

#### **`client.py`**
Gère l’exécution globale du projet et le chargement des modules.

#### **`config.py`**
Charge la configuration depuis un fichier YAML ou les variables d’environnement.

#### **`cli.py`**
Expose une interface en ligne de commande simple et extensible.

#### **`api.py`**
Fournit une API interne pour interagir avec ProjetRST.

#### **`modules/`**
Contient les modules fonctionnels (core, utils, etc.).

#### **`data/`**
Contient les données internes du projet.

---
