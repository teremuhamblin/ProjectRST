#!/usr/bin/env bash
# ==========================================
# Script : build_docs.sh
# Description : Génère la documentation Sphinx
# ==========================================

set -euo pipefail

DOCS_DIR="Docs(.rst)"
BUILD_DIR="$DOCS_DIR/_build"

echo "[INFO] Génération de la documentation Sphinx..."
sphinx-build -b html "$DOCS_DIR" "$BUILD_DIR"

echo "[INFO] Documentation générée dans : $BUILD_DIR"
