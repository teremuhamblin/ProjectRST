Architecture
============

L’architecture du projet repose sur trois piliers :

- Une documentation centralisée dans ``docs/``
- Un code source organisé dans ``src/``
- Une séparation claire entre API Vue d’ensemble
--------------

L’architecture de ProjetRST repose sur trois couches principales :

1. **Core** — logique interne et classes fondamentales.
2. **Modules** — extensions fonctionnelles optionnelles.
3. **Interface** — CLI, API, intégrations externes.

Schéma simplifié
----------------

.. code-block:: text

   +-----------------------+
   |       Interface       |
   +-----------------------+
   |        Modules        |
   +-----------------------+
   |         Core          |
   +-----------------------+
