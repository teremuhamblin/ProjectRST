# ============================
# Makefile — ProjetRST
# Automatisation : build, tests, docs, lint, format, release
# Compatible CI/CD & Windows (via Python)
# ============================

PYTHON      ?= python3
PIP         ?= pip
TESTS       ?= pytest
SPHINX      ?= sphinx-build
BLACK       ?= black
RUFF        ?= ruff
TWINE       ?= twine

SRC_DIR     := src
TEST_DIR    := tests
DOCS_DIR    := Docs(.rst)
BUILD_DIR   := $(DOCS_DIR)/_build
DIST_DIR    := dist

# ----------------------------
# Commandes principales
# ----------------------------

.PHONY: help install test docs clean run build lint format check release dist

help:
	@echo "Commandes disponibles :"
	@echo "  make install    - Installe les dépendances (dev inclus)"
	@echo "  make test       - Lance les tests unitaires"
	@echo "  make docs       - Génère la documentation Sphinx"
	@echo "  make clean      - Nettoie les fichiers temporaires et artefacts"
	@echo "  make run        - Exécute le client ProjetRST"
	@echo "  make build      - Build complet (lint + tests + docs)"
	@echo "  make lint       - Analyse statique (ruff)"
	@echo "  make format     - Formatage du code (black)"
	@echo "  make check      - Lint + tests (pour CI)"
	@echo "  make dist       - Build des artefacts Python (sdist + wheel)"
	@echo "  make release    - Build + upload (via twine)"

# ----------------------------
# Installation
# ----------------------------

install:
	$(PIP) install -e .
	@if [ -f requirements.txt ]; then $(PIP) install -r requirements.txt; fi
	@if [ -f pyproject.toml ]; then $(PIP) install ".[dev]" || true; fi

# ----------------------------
# Tests
# ----------------------------

test:
	$(TESTS) -vv $(TEST_DIR)

# ----------------------------
# Documentation
# ----------------------------

docs:
	$(SPHINX) -b html $(DOCS_DIR) $(BUILD_DIR)

# ----------------------------
# Nettoyage (cross-platform friendly)
# ----------------------------

clean:
	@echo "[INFO] Nettoyage des artefacts..."
	@$(PYTHON) - << "EOF"
import os, shutil
paths = [
    "$(BUILD_DIR)",
    "$(DIST_DIR)",
    ".pytest_cache",
]
for path in paths:
    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=True)
for root, dirs, files in os.walk("."):
    for d in list(dirs):
        if d == "__pycache__":
            shutil.rmtree(os.path.join(root, d), ignore_errors=True)
    for f in list(files):
        if f.endswith(".pyc") or f.endswith(".pyo"):
            try:
                os.remove(os.path.join(root, f))
            except OSError:
                pass
EOF
	@echo "[INFO] Nettoyage terminé."

# ----------------------------
# Exécution
# ----------------------------

run:
	$(PYTHON) -m projetrst.cli

# ----------------------------
# Lint & Format
# ----------------------------

lint:
	@echo "[INFO] Lint avec ruff..."
	$(RUFF) $(SRC_DIR) $(TEST_DIR)

format:
	@echo "[INFO] Formatage avec black..."
	$(BLACK) $(SRC_DIR) $(TEST_DIR)

check: lint test
	@echo "[INFO] Check complet (lint + tests) terminé."

# ----------------------------
# Build complet
# ----------------------------

build: lint test docs
	@echo "[INFO] Build complet terminé."

# ----------------------------
# Distribution & Release
# ----------------------------

dist:
	@echo "[INFO] Build des artefacts Python (sdist + wheel)..."
	$(PYTHON) -m build

release: clean dist
	@echo "[INFO] Upload via twine..."
	$(TWINE) upload dist/*
