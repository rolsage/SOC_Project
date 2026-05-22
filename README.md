# 🛡️ SOC & IPS Project - Surveillance Réseau & Détection d'Intrusions

Ce projet implémente une solution légère de **SOC (Security Operations Center)** et d'**IPS (Intrusion Prevention System)** conteneurisée avec Docker et dotée d'un tableau de bord analytique en temps réel avec Streamlit.

L'application capture le trafic réseau suspect, applique des règles de blocage automatique (pare-feu), et centralise les alertes (`LOGIN_FAILED`, `SQL_INJECTION`, `PORT_SCAN`, `XSS`) dans une interface graphique interactive.

---

## 🏗️ Architecture du Projet

Le projet est divisé en deux composants clés :
1. **Le Moteur de Détection (SOC/IPS)** : S'exécute dans un conteneur Docker isolé mais configuré en mode réseau `host` avec les capacités `NET_ADMIN`. Il analyse les flux et peut interagir directement avec le pare-feu du système pour bannir les IP malveillantes.
2. **Le Dashboard Visuel** : Une application Python locale basée sur **Streamlit** et **Plotly Express** qui lit le fichier de logs partagé (`network_traffic.log`) pour générer des statistiques et des graphiques dynamiques.

---

## 📋 Prérequis

Avant de lancer le projet, assurez-vous de disposer des outils suivants sur votre machine (optimisé pour **Kali Linux**) :

* Docker & Docker Compose
* Python 3.x
* Un environnement virtuel Python (`venv`)

---

## 🚀 Installation et Lancement

### 1. Cloner le dépôt et se positionner
```bash
git clone [https://github.com/rolsage/SOC_Project.git](https://github.com/rolsage/SOC_Project.git)
cd SOC_Project
