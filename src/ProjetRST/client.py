class Client:
    """
    Client principal de ProjetRST.
    Gère l'exécution globale et le chargement des modules.
    """

    def __init__(self):
        self.modules = []

    def load_modules(self):
        """Charge les modules disponibles."""
        from .modules.core import CoreModule
        from .modules.utils import UtilsModule

        self.modules = [
            CoreModule(),
            UtilsModule(),
        ]

    def run(self):
        """Exécute le processus principal."""
        self.load_modules()
        print("ProjetRST est en cours d'exécution...")
        for module in self.modules:
            module.execute()
