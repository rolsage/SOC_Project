import time
import os

def monitor_logs(filename):
    print(f"👀 Surveillance intelligente active sur {filename}...")
    stats_intrusions = {} # Dictionnaire pour compter les échecs par IP

    with open(filename, "r") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            
            if "LOGIN_FAILED" in line:
                # On extrait l'IP de la ligne (ex: 192.168.1.100)
                parts = line.split(", ")
                ip_address = parts[2].split(": ")[1]
                
                # Mise à jour du compteur
                stats_intrusions[ip_address] = stats_intrusions.get(ip_address, 0) + 1
                count = stats_intrusions[ip_address]

                print(f"⚠️  TENTATIVE DÉTECTÉE | IP: {ip_address} | Échecs: {count}")

                if count >= 3:
                    print(f"🚨 ALERTE CRITIQUE : Suspicion de Brute Force sur {ip_address} ! 🚨")
                print("-" * 30)

if __name__ == "__main__":
    monitor_logs("network_traffic.log")
