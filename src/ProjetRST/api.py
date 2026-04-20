"""
API interne de ProjetRST.
"""


class API:
    """Interface API simple pour interagir avec ProjetRST."""

    def status(self):
        return {"status": "running", "version": "1.0.0"}
