def run(user):
    print(f"[*] Simulation de test de droits ACL pour l'utilisateur : {user}")
    print("[+] (Démo) Accès à SYSVOL : autorisé")
    print("[+] (Démo) Accès à C$ : refusé")
    print("[+] (Démo) Tentative de lecture GPO : autorisée")