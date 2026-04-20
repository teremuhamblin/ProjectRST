"""
Gestion de la configuration de ProjetRST.
"""

import os
import yaml


class Config:
    """Charge et expose la configuration du projet."""

    def __init__(self, path=None):
        self.path = path or os.getenv("PROJetrst_CONFIG", "config.yaml")
        self.data = self._load()

    def _load(self):
        if not os.path.exists(self.path):
            return {}

        with open(self.path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}

    def get(self, key, default=None):
        return self.data.get(key, default)
