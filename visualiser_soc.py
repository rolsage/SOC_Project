import pandas as pd
import plotly.express as px

# Analyse des logs
failed_ips = []
with open("network_traffic.log", "r") as f:
    for line in f:
        if "LOGIN_FAILED" in line:
            # Extraction de l'IP
            ip = line.split("IP: ")[1].split(",")[0]
            failed_ips.append(ip)

# Création du tableau
df = pd.DataFrame(failed_ips, columns=['IP_Source'])
counts = df['IP_Source'].value_counts().reset_index()
counts.columns = ['IP_Source', 'Tentatives']

# Génération du graphique
fig = px.bar(counts, x='IP_Source', y='Tentatives', 
             title="Analyse SOC : Force Brute",
             color='Tentatives', color_continuous_scale='Reds')

# Sauvegarde
fig.write_image("alerte_intrusion.png")
print("✅ Succès ! L'image 'alerte_intrusion.png' a été créée.")
