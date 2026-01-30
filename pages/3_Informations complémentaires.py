import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")


import streamlit as st


st.markdown(
"""
# 📊 Variations des actions Fnac Darty sur 12 mois

Voici un résumé **chronologique** des principales fluctuations du cours de l’action Fnac Darty de février 2025 à janvier 2026, avec les causes principales :

---

## 1️⃣ Mars – début avril 2025 : Baisse importante
- **Événement** : Publication des objectifs de marge jugés modestes pour 2025 et résultats du 1er trimestre perçus comme mitigés.
- **Impact sur le cours** : Chute significative, le titre atteint son **plus bas de la période**.
- **Cause** : Déception des investisseurs face à la rentabilité anticipée et croissance organique limitée.

---

## 2️⃣ Avril 2025 : Stabilisation et légère reprise
- **Événement** : Confirmation d’une croissance légère du chiffre d’affaires et du plan d’intégration d’Unieuro.
- **Impact sur le cours** : Stabilisation autour des niveaux bas, quelques hausses ponctuelles.
- **Cause** : Atténuation des craintes après clarification des résultats.

---

## 3️⃣ Mai – Juin 2025 : Hausse liée au plan stratégique 2030
- **Événement** : Annonce du plan stratégique ambitieux « Beyond Everyday » (services récurrents, objectif de marge >3%, politique de dividende révisée).
- **Impact sur le cours** : Hausse notable (+10% sur certaines séances).
- **Cause** : Optimisme des investisseurs face aux perspectives de croissance à moyen/long terme.

---

## 4️⃣ Juillet 2025 : Baisse ponctuelle
- **Événement** : Publication de résultats semestriels jugés décevants et détachement du dividende début juillet.
- **Impact sur le cours** : Correction de l’action entre **18 et 31 juillet**.
- **Cause** : Effet technique du dividende + prises de bénéfices après une hausse antérieure.

---

## 5️⃣ Août – septembre 2025 : Stabilité et soutien par rachats d’actions
- **Événement** : Lancement de programmes de rachat d’actions pour réduire le flottant et soutenir le cours.
- **Impact sur le cours** : Stabilisation et légère reprise.
- **Cause** : Signal positif de confiance de la direction et amélioration des ratios financiers.

---

## 6️⃣ Octobre – décembre 2025 : Fluctuations modérées
- **Événement** : Résultats trimestriels positifs mais absence de catalyseurs majeurs.
- **Impact sur le cours** : Oscillations autour d’un plateau (28-32 €).
- **Cause** : Marché prudent, prises de bénéfices et tendances du retail général.

---

## 7️⃣ Janvier 2026 : Forte hausse
- **Événement** : Annonce d’une **OPA amicale** par Daniel Křetínský (EP Group), offrant une prime d’environ 19% sur le cours.
- **Impact sur le cours** : Hausse immédiate de +17 à +18% en quelques séances.
- **Cause** : Forte demande anticipée pour le rachat et signal de valorisation attractive pour les actionnaires.

"""
)


st.markdown("---")

st.markdown(
    "### 🔗 Pour explorer les données vous‑même"
)
st.markdown(
    "[Euronext](https://live.euronext.com/fr/product/equities/FR0011476928-XPAR)", 
    unsafe_allow_html=True
)


