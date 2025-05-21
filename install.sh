#!/bin/bash
echo "[*] Installation de RogueSuite sur Kali Linux..."

sudo apt update
sudo apt install -y python3 python3-pip
pip3 install -r requirements.txt

echo "[+] RogueSuite installé. Lancement par : python3 roguesuite.py run scripts/insider_simulation.yaml"