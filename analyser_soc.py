import pandas as pd

print("\n--- Analyse des logs en cours ---")
with open("network_traffic.log", "r") as f:
    lines = f.readlines()

failed_attempts = {}
threshold = 3 

for line in lines:
    if "LOGIN_FAILED" in line:
        ip = line.split("IP: ")[1].split(",")[0]
        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
        
        if failed_attempts[ip] >= threshold:
            print(f"⚠️  ALERTE : Force Brute détectée depuis {ip} ({failed_attempts[ip]} échecs) !")

print("--- Analyse terminée ---\n")
