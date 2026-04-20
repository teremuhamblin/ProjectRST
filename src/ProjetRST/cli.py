"""
Interface en ligne de commande (CLI) de ProjetRST.
"""

import argparse
from .client import Client


def main():
    parser = argparse.ArgumentParser(description="CLI de ProjetRST")
    parser.add_argument("--verbose", action="store_true", help="Mode verbeux")

    args = parser.parse_args()

    client = Client()

    if args.verbose:
        print("[DEBUG] Mode verbeux activé")

    client.run()
