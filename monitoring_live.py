import time
import os
import subprocess

def bloquer_ip(ip):
    print(f"🛡️ ACTION DE DÉFENSE : Blocage définitif de l'IP {ip}...")
    try:
        # Configuration propre pour injecter la règle dans le pare-feu Linux
        subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)
        print(f"✅ IP {ip} bannie avec succès au niveau du pare-feu.")
    except Exception as e:
        print(f"❌ Erreur système lors du blocage : {e}")

def monitor_logs(filename):
    print(f"🚨 SOC PROTECT : Surveillance et Protection Active sur {filename}...")
    stats_intrusions = {}

    # Si le fichier n'existe pas encore, on le crée pour éviter un crash
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            pass

    with open(filename, "r") as f:
        # On se place à la fin du fichier pour ne lire que les nouveaux événements
        f.seek(0, os.SEEK_END)
        
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            
            if "LOGIN_FAILED" in line and "," in line:
                try:
                    parts = line.split(", ")
                    ip_address = parts[2].split(": ")[1].strip()
                    
                    stats_intrusions[ip_address] = stats_intrusions.get(ip_address, 0) + 1
                    count = stats_intrusions[ip_address]

                    print(f"⚠️  TENTATIVE DÉTECTÉE : IP {ip_address} | Échecs cumulés : {count}")

                    # Déclenchement de la sécurité au bout de 3 alertes
                    if count == 3:
                        bloquer_ip(ip_address)
                    elif count > 3:
                        print(f"🚫 IP {ip_address} est déjà verrouillée par le pare-feu.")
                    
                    print("-" * 40)
                except IndexError:
                    # Sécurité si une ligne du log est mal écrite ou corrompue
                    continue

if __name__ == "__main__":
    monitor_logs("network_traffic.log")
