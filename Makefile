# ============================
# Makefile — ProjetRST
# Automatisation : build, tests, docs
# ============================

PYTHON=python3
PIP=pip
SPHINXBUILD=sphinx-build
TESTS=pytest

# ----------------------------
# Commandes principales
# ----------------------------

help:
	@echo "Commandes disponibles :"
	@echo "  make install     - Installe les dépendances"
	@echo "  make test        - Lance les tests unitaires"
	@echo "  make docs        - Génère la documentation Sphinx"
	@echo "  make clean       - Nettoie les fichiers temporaires"
	@echo "  make run         - Exécute le client ProjetRST"
	@echo "  make build       - Build complet (tests + docs)"

install:
	$(PIP) install -e .
	$(PIP) install -r requirements.txt || true

test:
	$(TESTS) -vv

docs:
	$(SPHINXBUILD) -b html Docs(.rst)/ Docs(.rst)/_build/

clean:
	rm -rf Docs(.rst)/_build/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

run:
	$(PYTHON) -m projetrst.cli

build: test docs
	@echo "Build complet terminé."
