"""
Tests avancés pour ProjetRST.
Inclut :
- mock
- patch
- exceptions
- tests CLI
- tests API
- tests modules
- tests config
- tests d'intégration
"""

import pytest
from unittest.mock import patch, MagicMock

from projetrst.client import Client
from projetrst.api import API
from projetrst.config import Config
from projetrst.modules.core import CoreModule
from projetrst.modules.utils import UtilsModule


# ---------------------------------------------------------
# FIXTURES AVANCÉES
# ---------------------------------------------------------

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def api():
    return API()

@pytest.fixture
def config(tmp_path):
    """Fixture avec fichier YAML temporaire."""
    cfg = tmp_path / "config.yaml"
    cfg.write_text("app:\n  debug: true\n")
    return Config(path=str(cfg))


# ---------------------------------------------------------
# TESTS CLIENT (avec mock)
# ---------------------------------------------------------

def test_client_load_modules_mock(client):
    with patch("projetrst.client.CoreModule") as mock_core:
        mock_instance = MagicMock()
        mock_core.return_value = mock_instance

        client.load_modules()
        assert len(client.modules) >= 1
        mock_core.assert_called_once()


def test_client_run_output(client, capsys):
    client.run()
    captured = capsys.readouterr()
    assert "ProjetRST est en cours d'exécution" in captured.out


# ---------------------------------------------------------
# TESTS API
# ---------------------------------------------------------

def test_api_status(api):
    status = api.status()
    assert status["status"] == "running"
    assert "version" in status


# ---------------------------------------------------------
# TESTS CONFIG (exceptions + patch)
# ---------------------------------------------------------

def test_config_missing_file():
    cfg = Config(path="fichier_inexistant.yaml")
    assert cfg.data == {}


def test_config_env_override(monkeypatch, tmp_path):
    cfg_file = tmp_path / "override.yaml"
    cfg_file.write_text("app:\n  log_level: DEBUG\n")

    monkeypatch.setenv("PROJetrst_CONFIG", str(cfg_file))

    cfg = Config()
    assert cfg.get("app")["log_level"] == "DEBUG"


# ---------------------------------------------------------
# TESTS MODULES (mock + patch)
# ---------------------------------------------------------

def test_core_module_execute(capsys):
    module = CoreModule()
    module.execute()
    captured = capsys.readouterr()
    assert "CoreModule" in captured.out


def test_utils_module_execute(capsys):
    module = UtilsModule()
    module.execute()
    captured = capsys.readouterr()
    assert "UtilsModule" in captured.out


# ---------------------------------------------------------
# TESTS CLI (simulation + patch)
# ---------------------------------------------------------

def test_cli_main(capsys):
    from projetrst.cli import main
    main()
    captured = capsys.readouterr()
    assert "ProjetRST est en cours d'exécution" in captured.out


# ---------------------------------------------------------
# TESTS D’INTÉGRATION
# ---------------------------------------------------------

def test_full_integration(client, capsys):
    """
    Test complet :
    - chargement modules
    - exécution client
    - capture sortie
    """
    client.run()
    captured = capsys.readouterr()
    assert "ProjetRST est en cours d'exécution" in captured.out
    assert len(client.modules) > 0
