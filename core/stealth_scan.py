import socket
import time
import random

def run():
    print("[*] Scan furtif sur la plage 192.168.1.0/24")
    for i in range(1, 10):
        ip = f"192.168.1.{i}"
        try:
            sock = socket.socket()
            sock.settimeout(0.3)
            sock.connect((ip, 445))
            print(f"[+] Port 445 ouvert sur {ip}")
        except:
            pass
        time.sleep(random.uniform(1.0, 2.5))  # Scan lent