"""
Tests complets pour ProjetRST.
Ce fichier couvre :
- Client
- API
- Configuration
- Modules
- CLI (exécution simulée)
"""

import pytest
from projetrst.client import Client
from projetrst.api import API
from projetrst.config import Config
from projetrst.modules.core import CoreModule
from projetrst.modules.utils import UtilsModule


# ---------------------------------------------------------
# FIXTURES
# ---------------------------------------------------------

@pytest.fixture
def client():
    """Fixture pour instancier le client."""
    return Client()


@pytest.fixture
def api():
    """Fixture pour instancier l'API."""
    return API()


@pytest.fixture
def config():
    """Fixture pour charger la configuration."""
    return Config()


# ---------------------------------------------------------
# TESTS CLIENT
# ---------------------------------------------------------

def test_client_initialisation(client):
    assert client.modules == []


def test_client_load_modules(client):
    client.load_modules()
    assert len(client.modules) >= 2


def test_client_run(client, capsys):
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
# TESTS CONFIG
# ---------------------------------------------------------

def test_config_default_load(config):
    assert isinstance(config.data, dict)


def test_config_get_default(config):
    assert config.get("unknown_key", "fallback") == "fallback"


# ---------------------------------------------------------
# TESTS MODULES
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
# TESTS CLI (simulation)
# ---------------------------------------------------------

def test_cli_execution(capsys):
    """
    Teste la CLI en simulant l'appel du main().
    """
    from projetrst.cli import main
    main()
    captured = capsys.readouterr()
    assert "ProjetRST est en cours d'exécution" in captured.out
