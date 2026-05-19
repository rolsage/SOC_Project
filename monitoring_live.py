import time
import os
import subprocess
import requests

# 🔴 COLLE TA VRAIE CLÉ API ABUSEIPDB ENTRE LES GUILLEMETS ICI :
API_KEY = "8997efac5d1375b704270fd63b2ee24887fe16ee08c19934ff9582582960bf7e28ae33c371661434"

def verifier_reputation_ip(ip):
    """ Interroge la base mondiale AbuseIPDB pour connaître le niveau de menace """
    url = "https://api.abuseipdb.com/api/v2/check"
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }
    headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }
    
    try:
        # Sécurité si la clé n'a pas été modifiée
        if API_KEY == "VOTRE_CLE_API_ICI" or API_KEY == "":
            print("❌ ERREUR : Tu as oublié de coller ta clé API à la ligne 7 !")
            return 0

        # Requête vers les serveurs d'AbuseIPDB
        response = requests.get(url, headers=headers, params=querystring, timeout=5)
        
        # Si la requête réussit (Code 200 OK)
        if response.status_code == 200:
            data = response.json()
            score_abus = data['data']['abuseConfidenceScore']
            return score_abus
        
        # Si le serveur refuse la clé ou rencontre un problème (Ex: 401 Unauthorized, 403 Forbidden)
        else:
            print(f"⚠️ Erreur AbuseIPDB : Code HTTP {response.status_code}")
            if response.status_code == 401 or response.status_code == 403:
                print("   👉 Vérifie que la clé API copiée-collée à la ligne 7 est exacte et active.")
            return 0
            
    except Exception as e:
        print(f"❌ Impossible de contacter l'API (Erreur réseau/DNS) : {e}")
        return 0

def bloquer_ip(ip, raison):
    print(f"🛡️ ACTION DE DÉFENSE : Blocage de l'IP {ip} ({raison})...")
    try:
        subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)
        print(f"✅ IP {ip} bannie avec succès au niveau du pare-feu.")
    except Exception as e:
        print(f"❌ Erreur système lors du blocage iptables : {e}")

def monitor_logs(filename):
    print(f"🚨 SOC INTEL : Surveillance proactive activée...")
    stats_intrusions = {}

    if not os.path.exists(filename):
        with open(filename, "w") as f: pass

    with open(filename, "r") as f:
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
                    
                    print(f"\n🔍 Analyse de l'IP entrante : {ip_address}")
                    
                    # Interrogation de la Threat Intelligence
                    score_danger = verifier_reputation_ip(ip_address)
                    print(f"🌐 Threat Intel Score : {score_danger}% de suspicion mondiale.")

                    # RÈGLE PROACTIVE : Si l'IP est globalement malveillante (> 50%), blocage immédiat !
                    if score_danger >= 50:
                        bloquer_ip(ip_address, f"Score mondial critique : {score_danger}%")
                        print("-" * 40)
                        continue

                    # RÈGLE LOCALE : Sinon, règle classique des 3 échecs locaux
                    stats_intrusions[ip_address] = stats_intrusions.get(ip_address, 0) + 1
                    count = stats_intrusions[ip_address]
                    print(f"⚠️  Activité locale : Échecs cumulés : {count}/3")

                    if count == 3:
                        bloquer_ip(ip_address, "Seuil local de 3 échecs atteint")
                    
                    print("-" * 40)
                except IndexError:
                    continue

if __name__ == "__main__":
    monitor_logs("network_traffic.log")
