import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. Configuration de la page Streamlit
st.set_page_config(page_title="Dashboard SOC - Surveillance Réseau", layout="wide")
st.title("🛡️ Dashboard Sécurité Opérationnelle (SOC)")

# 2. Chemin vers le fichier de logs partagé
LOG_FILE = "network_traffic.log"

st.subheader("Analyse du Trafic et Détection des Intrusions en Temps Réel")

# 3. Vérification et lecture des données de trafic
if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 0:
    try:
        # CORRECTION : Alignement exact avec la structure de tes logs réels
        # Horodatage, Type d'événement (LOGIN_FAILED), IP cible, Utilisateur ciblé, etc.
        df = pd.read_csv(LOG_FILE, names=["Horodatage", "Type_Attaque", "IP_Cible", "Identifiant", "Vide1", "Vide2", "Vide3"])
        
        # Nettoyage cosmétique pour l'affichage du tableau
        df_affichage = df[["Horodatage", "Type_Attaque", "IP_Cible", "Identifiant"]].copy()
        
        # Affichage du tableau de données brutes réalignées
        st.write("### Dernières alertes enregistrées")
        st.dataframe(df_affichage.tail(10), use_container_width=True)
        
        # 4. Génération du graphique des attaques
        st.write("### Répartition des Types d'Attaques")
        if "Type_Attaque" in df.columns and not df["Type_Attaque"].dropna().empty:
            df_counts = df["Type_Attaque"].value_counts().reset_index()
            df_counts.columns = ["Type d'Attaque", "Nombre"]
            
            fig = px.bar(df_counts, x="Type d'Attaque", y="Nombre", color="Type d'Attaque", 
                         title="Alertes détectées par catégorie", barmode="group")
            
            # Sauvegarde de l'image
            fig.write_image("alerte_intrusion.png")
            
            # Affichage direct sur le navigateur
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Aucune attaque spécifique répertoriée dans les logs pour le moment.")
            
    except Exception as e:
        st.error(f"Erreur lors de la lecture des données : {e}")
else:
    st.info(f"En attente de données... Le fichier de logs ({LOG_FILE}) est vide ou n'a pas encore été généré par le moteur.")
