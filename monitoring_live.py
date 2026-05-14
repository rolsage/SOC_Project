import time
import os

def monitor_logs(filename):
    print(f"👀 Surveillance active sur {filename}...")
    
    # On ouvre le fichier et on va à la fin
    with open(filename, "r") as f:
        f.seek(0, os.SEEK_END)
        
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1) 
                continue
            
            # Détection d'alerte
            if "LOGIN_FAILED" in line:
                print(f"⚠️  ALERTE : Tentative d'intrusion détectée !")
                print(f"🔍 Détails : {line.strip()}")
                print("-" * 30)

if __name__ == "__main__":
    monitor_logs("network_traffic.log")
