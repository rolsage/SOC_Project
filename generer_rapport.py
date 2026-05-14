import pandas as pd
import os

def creer_rapport_html(log_file):
    print("📊 Génération du rapport d'incidents en cours...")
    
    if not os.path.exists(log_file):
        print(f"❌ Erreur : Le fichier {log_file} est introuvable.")
        return

    data = []
    with open(log_file, "r") as f:
        for line in f:
            # On vérifie que la ligne contient bien une alerte et les séparateurs attendus
            if "LOGIN_FAILED" in line and "," in line:
                parts = line.split(", ")
                # Sécurité : on vérifie qu'on a bien les 4 colonnes (Date, Statut, IP, User)
                if len(parts) >= 4:
                    try:
                        data.append({
                            "Date": parts[0],
                            "Statut": parts[1],
                            "IP": parts[2].split(": ")[1],
                            "Utilisateur": parts[3].split(": ")[1].strip()
                        })
                    except IndexError:
                        continue # Saute la ligne si le format est bizarre

    if not data:
        print("⚠️ Aucune donnée d'intrusion trouvée dans les logs.")
        return

    df = pd.DataFrame(data)
    
    # Création du design du rapport
    html_content = f"""
    <html>
    <head>
        <title>Rapport SOC - Alertes</title>
        <style>
            body {{ font-family: Arial; margin: 40px; background-color: #f4f4f4; }}
            h1 {{ color: #d9534f; border-bottom: 2px solid #d9534f; padding-bottom: 10px; }}
            table {{ border-collapse: collapse; width: 100%; background: white; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
            th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }}
            th {{ background-color: #d9534f; color: white; }}
            tr:hover {{ background-color: #f5f5f5; }}
        </style>
    </head>
    <body>
        <h1>🚨 Rapport d'Incidents de Sécurité (SOC)</h1>
        <p>Ce rapport liste les tentatives d'accès non autorisées détectées en temps réel.</p>
        {df.to_html(index=False)}
        <p style="margin-top: 20px; font-size: 0.8em; color: gray;">Généré par le système de surveillance de Roland.</p>
    </body>
    </html>
    """
    
    with open("rapport_incidents.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print("✅ Rapport généré avec succès : rapport_incidents.html")

if __name__ == "__main__":
    creer_rapport_html("network_traffic.log")
