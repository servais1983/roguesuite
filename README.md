# RogueSuite – Red Team Stealth CLI

Simulateur d'attaques internes discrètes pour tester les capacités de détection Blue Team.

## 🧠 Modules

- `scan` : Scan réseau furtif (slow + random)
- `acl --user` : Simulation de test d'accès AD
- `noise` : Génère du trafic DNS/beacon discret
- `run` : Lance un scénario YAML complet

## 🛠️ Installation

```bash
chmod +x install.sh
./install.sh
```

## 🚀 Exemple d'utilisation

```bash
python3 roguesuite.py run scripts/insider_simulation.yaml
```

Utiliser uniquement dans des environnements de test autorisés.