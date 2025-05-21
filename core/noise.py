import random
import time
import socket

def run():
    print("[*] Injection de bruit réseau (DNS et beacon)")
    domains = ["update-check.win", "internal-ping.org", "metrics.fake"]
    for _ in range(5):
        domain = random.choice(domains)
        try:
            socket.gethostbyname(domain)
            print(f"[~] DNS query vers {domain}")
        except:
            pass
        time.sleep(random.uniform(0.5, 1.5))

    print("[~] Simulation de beacon HTTP (sans payload)...")
    for _ in range(3):
        print("[>] Beacon vers 10.0.0.5:8080 simulé")
        time.sleep(random.uniform(1.5, 3.0))