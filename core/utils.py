import yaml
from core import stealth_scan, acl_test, noise

def run_script_yaml(path):
    print(f"[*] Chargement du scénario : {path}")
    with open(path, "r") as f:
        data = yaml.safe_load(f)

    for step in data.get("steps", []):
        if step["type"] == "scan":
            stealth_scan.run()
        elif step["type"] == "acl":
            acl_test.run(step.get("user", "unknown"))
        elif step["type"] == "noise":
            noise.run()
        else:
            print(f"[!] Étape inconnue : {step}")