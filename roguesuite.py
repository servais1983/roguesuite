#!/usr/bin/env python3

import argparse
from core import stealth_scan, acl_test, noise
from core.utils import run_script_yaml

def main():
    parser = argparse.ArgumentParser(prog="roguesuite", description="Simulateur d'attaques internes furtives")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("scan", help="Scan low-and-slow")

    acl = subparsers.add_parser("acl", help="Test de droits ACL AD simulés")
    acl.add_argument("--user", required=True)

    subparsers.add_parser("noise", help="Génère du bruit réseau discret")

    run = subparsers.add_parser("run")
    run.add_argument("file", help="Fichier YAML de scénario")

    args = parser.parse_args()

    if args.command == "scan":
        stealth_scan.run()
    elif args.command == "acl":
        acl_test.run(args.user)
    elif args.command == "noise":
        noise.run()
    elif args.command == "run":
        run_script_yaml(args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()