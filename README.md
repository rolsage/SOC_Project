# 🚨 SOC & IPS Project - Automated Threat Intelligence

Ce projet consiste en la création d'un mini **SOC (Security Operations Center)** et d'un **IPS (Intrusion Prevention System)** automatisé en Python sous Kali Linux. Il permet de surveiller les journaux d'accès réseau en temps réel, de détecter les comportements malveillants et d'appliquer des contre-mesures immédiates.

## 🌟 Fonctionnalités Clés

* **Surveillance Active :** Analyse en temps réel des fichiers de logs réseau (`network_traffic.log`).
* **Défense Locale Automatisée (IPS) :** Blocage dynamique des adresses IP suspectes via le pare-feu Linux `iptables` après 3 tentatives de connexion infructueuses (`LOGIN_FAILED`).
* **Intégration Threat Intelligence Mondiale :** Connexion via API à la base de données globale **AbuseIPDB**.
* **Défense Proactive :** Analyse instantanée de la réputation de chaque IP entrante. Si l'IP possède un score de suspicion mondiale supérieur à 50%, elle est bannie dès sa première tentative par anticipation.

## 🛠️ Technologies Utilisées

* **Système :** Kali Linux
* **Langage :** Python 3 (Modules : `requests`, `subprocess`, `os`, `time`)
* **Sécurité & Réseau :** Netfilter / `iptables` (Pare-feu Linux)
* **Cyber-Intelligence :** API AbuseIPDB v2

## 🚀 Comment l'utiliser

1. Cloner le dépôt :
   ```bash
   git clone
