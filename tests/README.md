###### README.md - markdown
# ProjetRST
### 📁 Dossier tests/
>Tests de ProjetRST
- Le dossier `tests/` contient l’ensemble des tests unitaires et fonctionnels du projet ProjetRST.  
- Il permet de garantir la stabilité, la qualité et le bon fonctionnement du code situé dans `src/`.

---

### 📦 Structure
```text
tests/
├── test_client.py
├── test_api.py
└── test_modules.py
```
>(Les fichiers ci‑dessus sont des exemples — ajoute ou modifie selon tes besoins.)

---

### 🎯 Objectifs des tests

- Vérifier le comportement des composants principaux  
- Assurer la non‑régression lors des mises à jour  
- Faciliter la maintenance et l’évolution du projet  
- Documenter les comportements attendus  

---

### ▶️ Exécuter les tests
>Depuis la racine du projet :
```bash
pytest
```

Ou avec plus de détails :
```bash
pytest -vv
```

---

🧪 Bonnes pratiques

- Un fichier de test par module  
- Des noms explicites : test_<fonction>.py  
- Des tests courts, isolés et reproductibles  
- Utiliser pytest pour sa simplicité et sa puissance  

---

📄 Licence

ProjetRST est distribué sous licence MIT.

---
