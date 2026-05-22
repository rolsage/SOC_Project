# 🛡️ Cybersécurité & IA : Network Analysis & SOC Project

Ce projet présente le déploiement d'un **Mini-SOC (Security Operations Center)** et d'un système de détection/prévention des intrusions (IDS/IPS) conteneurisé, couplé à un tableau de bord d'analyse de trafic en temps réel.

## 🚀 Fonctionnalités
* **Moteur de Détection (Docker) :** Analyse du trafic réseau, détection des attaques par force brute (`LOGIN_FAILED`), scans de ports et injections.
* **Atténuation automatique :** Bannissement des adresses IP malveillantes via des règles de pare-feu.
* **Dashboard Interactif (Streamlit & Plotly) :** Visualisation graphique en temps réel des alertes de sécurité et monitoring du trafic.

## 🛠️ Technologies Utilisées
* **OS / Environnement :** Kali Linux
* **Conteneurisation :** Docker, Docker Compose
* **Langages :** Python (Pandas, Streamlit, Plotly, Kaleido)
* **Sécurité :** Analyse de logs réseau, détection de patterns d'attaques

## 📊 Capture d'Écran du Dashboard
L'interface Streamlit génère une répartition dynamique des attaques détectées :
* Alertes d'authentification échouées (`LOGIN_FAILED`)
* Tentatives d'injections et scans de ports ciblés
