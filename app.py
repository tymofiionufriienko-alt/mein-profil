import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dein Name – Profil", page_icon="👋", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.image("profilbild.jpg", width=180)
    st.title("Tymofii Onufriienko")
    st.caption("UHH / BWL · Hamburg, Altona")
    st.markdown("**Daten, Prozessen, Technologien.**")
    st.write("Als Stunden in Wirtschaftswissenschaften verbinden ich analytische Stärke mit echter Macher-Mentalität und Kommunikationsfreude. Ein internationales Umfeld mit flachen Hierarchien, direckten Einfluss und frühere Verantwortungsübernahme bilden der idealle Grundlage zum Wachsen.")
    st.markdown("**Fokus:** Controlling & BI · Prozess- & Projektmanagement · Operations & SCM · Quality Analytics")
    st.divider()
    st.markdown("**Kontakt & Links**")
    st.markdown("- 📧 tymofii.onufriienko@gmail.com")
    st.markdown("- 🔗 [LinkedIn](https://linkedin.com)")
    st.markdown("- 💻 [GitHub](https://github.com)")

# --- HAUPTBEREICH ---
st.title("Hi, ich bin Timo 👋")
st.subheader("Scrollen, klicken, kennenlernen: Mein interaktives Bewerbungsprofil.")

tab1, tab2, tab3 = st.tabs(["Über mich", "Projekte & Erfahrung", "Skills & Tools"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Mein Fokus")
        st.markdown("- **Zahlen und Datenaffinität**")
        st.write(
            "Ich habe ein solides Fundament in Wirtschaftsinformatik, Bilanzierung, Mathematik und Statistik beherrsche Excel (komplexe Formeln, Pivot-Tabellen, Datenbereinigung) sowie Access und SQL und bringe vertieftes Fachwissen im Qualitätsmanagement (ISO 9001) mit."
        )
        st.markdown("- **Gelebte Eigeninitiative und Führung**")
        st.write("Als mehrfach gewählter Vorstand rede ich nicht nur über Organisation, sondern löse täglich echte Probleme pragmatisch und übernehme Verantwortung.")
        st.markdown("- **Inerkulturelle Brückenbauer**")
        st.write("Durch mien internationales Wohnumfeld und vier Sprachen (Ukrainisch, Russisch, Deutsch, Englisch) gehe ich offen auf Menschen zu und baue mühelos Netzwerke über Abteilungsgrenzen hinweg auf.")
        st.markdown("- **Stressresistenz & Bodenständigkeit**")
        st.write("Jobs im Einzelhandel und der Gastronomie haben mir gezeigt, wie das operative Tagesgeschäft an der Basis läuft und wie man auch bei Engpässen einen kühlen Kopf bewahrt.")
        st.markdown("- **Detailgenauigkeit & Lernhunger**")
        st.write("Ich erledige Aufgaben zuverlässig bis zum Abschluss, brennst darauf, mich mit erfahrenen Experten zu umgeben, und bringst eine kreative Seite mit.")
    with col2:
        st.markdown("### Kennzahlen auf einen Blick")
        
        # Erste Reihe
        m1, m2 = st.columns(2)
        m1.metric("BWL-Studium (UHH)", "3. Semester", "60+ ECTS")
        m2.metric("Abi-Ø", "1,7", "Top 15%")
        
        st.write("") # Kleiner vertikaler Abstand zwischen den Reihen
        
        # Zweite Reihe
        m3, m4 = st.columns(2)
        m3.metric("Sprachen", "3 fließend", "DE · EN · UKR · RU")
        m4.metric("Verfügbarkeit", "20 Std./Woche", "Ab sofort bereit")
with tab2:
    st.markdown("### Ausgewählte Stationen & Projekte")
    
    with st.expander("Projekt 1: Financial Tracker (Excel & Datenanalyse)", expanded=True):
        st.write("**Problem:** Unübersichtliche manuelle Ausgaben- und Finanzverfolgung.")
        st.write("**Lösung:** Strukturierter Financial Tracker in Excel mit automatisierten Auswertungen.(nich reale Daten und sicher zum herunterladen:)")
        
        # 1. Excel-Datei einlesen und Tabellenblätter anzeigen
        excel_datei = "financial_tracker.xlsx"
        xls = pd.ExcelFile(excel_datei)
       
        
        
        # 3. Download-Button für den Arbeitgeber
        with open(excel_datei, "rb") as file:
            st.download_button(
                label="📥 Financial Tracker (.xlsx) herunterladen",
                data=file,
                file_name="Financial_Tracker_Tymofii_Onufriienko.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

   
with tab3:
    st.markdown("### Hard Skills")
    
    # 1. Die 4 Kategorien als übersichtliche Liste (wie in deinem Beispielbild)
    st.markdown("""
    - 👨‍💻 **Programming:** Python (Streamlit, Pandas, vibe-coding), SQL
    - 📊 **Data Visualization:** MS Office, MS Excel, Miro, Slack
    - 📚 **Econ & Data analytics:** Accountig, Linear Regression, Decision Trees
    - 🖥️ **Databases:** SQL, MS Access
    """)
    
    st.divider()
    
   # 2. Schmale Balken exakt für deine 5 Skills & neuen Kategorien
    st.markdown("#### Skill-Level im Detail")
    skills = pd.DataFrame({
        "Skill": ["Python", "SQL", "Excel", "MS Office", "Access"],
        "Kategorie": ["Programming", "Programming", "Data Visualization", "Data Visualization", "Databases"],
        "Level": [70, 60, 90, 90, 80]
    })
    
    kategorie = st.selectbox("Nach Bereich filtern:", ["Alle"] + list(skills["Kategorie"].unique()))
    gefiltert = skills if kategorie == "Alle" else skills[skills["Kategorie"] == kategorie]
    
    col_chart, _ = st.columns([1, 1])
    with col_chart:
        st.vega_lite_chart(
            gefiltert,
            {
                "mark": {"type": "bar", "width": 22, "color": "#4da6ff", "cornerRadiusEnd": 4},
                "encoding": {
                    "x": {"field": "Skill", "type": "nominal", "sort": None, "axis": {"labelAngle": 0, "title": None}},
                    "y": {"field": "Level", "type": "quantitative", "scale": {"domain": [0, 100]}, "axis": {"title": "Level (%)"}}
                },
                "height": 300
            },
            use_container_width=True
        )