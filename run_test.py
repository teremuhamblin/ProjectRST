#!/usr/bin/env python3
"""
Script d'exécution des tests pour ProjetRST.
Permet de lancer pytest directement via Python.
"""

import pytest
import sys

def main():
    print("🔍 Exécution des tests ProjetRST...")
    exit_code = pytest.main(["-vv"])
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
