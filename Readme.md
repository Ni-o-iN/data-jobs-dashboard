# 💼 Data & AI Jobs Dashboard

Ein interaktives Streamlit-Dashboard zur Visualisierung und Analyse von Data- und AI-Jobs aus der RemoteOK API.

![Python](https://img.shields.io/badge/Python-3.14.2+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📋 Inhaltsverzeichnis

- [Über das Projekt](#über-das-projekt)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Technologien](#technologien)
- [Projekt-Struktur](#projekt-struktur)
- [API-Informationen](#api-informationen)
- [Mögliche Erweiterungen](#mögliche-erweiterungen)
- [Learnings](#learnings)
- [Kontakt](#kontakt)
- [Lizenz](#lizenz)

## 🎯 Über das Projekt

Dieses Projekt ist ein **interaktives Dashboard** zur Exploration des Data- und AI-Jobmarktes. Es nutzt die RemoteOK API, um aktuelle Remote-Jobs zu laden, filtert diese nach relevanten Keywords und visualisiert die Ergebnisse übersichtlich.

**Motivation:** Als angehender Data-Professional wollte ich den Jobmarkt besser verstehen und gleichzeitig praktische Erfahrung mit APIs, Datenvisualisierung und Web-Dashboards sammeln.

## ✨ Features

- 🔍 **Automatische Filterung** - Findet Data/AI-relevante Jobs aus 95+ Remote-Positionen
- 📊 **Interaktive Visualisierungen** - Pie Chart für Top-Kategorien
- 📋 **Übersichtliche Tabelle** - Alle gefilterten Jobs auf einen Blick
- 📈 **Key Metrics** - Schneller Überblick über Anzahl der Jobs
- 🔄 **Live-Daten** - Aktualisiert bei jedem Laden der Seite
- 💻 **Responsive Design** - Wide-Layout für bessere Übersicht

## 🖼️ Demo

### Dashboard-Ansicht
*[Screenshot hier einfügen]*

### Pie Chart - Top Job-Kategorien
*[Screenshot hier einfügen]*

### Job-Tabelle
*[Screenshot hier einfügen]*

## 🚀 Installation

### Voraussetzungen

- Python 3.9 oder höher
- pip (Python Package Manager)
- Git (optional, zum Klonen)

### Schritt-für-Schritt Anleitung

1. **Repository klonen** (oder als ZIP herunterladen):
   ```bash
   git clone https://github.com/DEIN-USERNAME/data-jobs-dashboard.git
   cd data-jobs-dashboard
   ```

2. **Virtual Environment erstellen** (empfohlen):
   
   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
   **Mac/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Dependencies installieren:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Dashboard starten:**
   ```bash
   streamlit run app.py
   ```

5. **Browser öffnen:**
   - Das Dashboard öffnet sich automatisch unter `http://localhost:8501`
   - Falls nicht, öffne den Link manuell im Browser

## 💡 Verwendung

### Dashboard-Funktionen

1. **Key Metrics (oben)**
   - Zeigt die Gesamtanzahl aller Jobs
   - Zeigt gefilterte Data/AI-Jobs

2. **Top 10 Job-Kategorien (Pie Chart)**
   - Visualisiert die häufigsten Tags in Data/AI-Jobs
   - Interaktiv: Hover für Details

3. **Job-Tabelle**
   - Alle gefilterten Jobs mit Position, Company, Location, Tags
   - Scrollbar bei vielen Einträgen
   - Sortierbar durch Klick auf Spaltenüberschriften

### Filter-Keywords

Das Dashboard filtert Jobs nach folgenden Keywords:
- `data`
- `ai`
- `machine learning`
- `ml`

Jobs werden gefunden, wenn diese Keywords in:
- Position/Job-Titel
- Tags

vorkommen.

## 🛠️ Technologien

| Technologie | Verwendung |
|------------|-----------|
| **Python 3.9+** | Programmiersprache |
| **Streamlit** | Web-Dashboard Framework |
| **Plotly Express** | Interaktive Visualisierungen |
| **Requests** | API-Calls |
| **Collections (Counter)** | Daten-Aggregation |

## 📁 Projekt-Struktur

```
data-jobs-dashboard/
│
├── app.py                 # Haupt-Dashboard-Anwendung
├── requirements.txt       # Python-Dependencies
├── README.md             # Diese Datei
├── .gitignore            # Git-Ignore-Regeln
└── venv/                 # Virtual Environment (lokal)
```

## 🌐 API-Informationen

### RemoteOK API

- **Endpoint:** `https://remoteok.com/api`
- **Typ:** REST API
- **Authentifizierung:** Keine (öffentlich)
- **Rate Limit:** Fair Use (nicht spammen)
- **Datenformat:** JSON

**Beispiel-Response:**
```json
{
  "id": "123456",
  "position": "Data Scientist",
  "company": "Example Corp",
  "location": "🌍 Worldwide",
  "tags": ["data", "python", "remote"],
  "url": "https://remoteok.com/remote-jobs/123456"
}
```

**Hinweis:** Die API liefert hauptsächlich Job-Kategorien als Tags (z.B. "engineer", "senior"), weniger technische Skills (z.B. "python", "pandas").

## 🔮 Mögliche Erweiterungen

### Kurzfristig (1-2 Tage)
- [ ] **Filter-Sidebar** - Nach Company, Location, Tags filtern
- [ ] **Balkendiagramm** - Top 10 Companies mit den meisten Jobs
- [ ] **Export-Funktion** - Gefilterte Jobs als CSV herunterladen
- [ ] **Link zu Jobs** - Direkter Link zur Stellenanzeige

### Mittelfristig (1 Woche)
- [ ] **Mehrere APIs** - Adzuna, Arbeitnow kombinieren
- [ ] **Tech-Stack Parsing** - Job-Descriptions nach Python, SQL, etc. durchsuchen
- [ ] **Gehaltsinformationen** - Visualisierung wenn vorhanden
- [ ] **Speicherfunktion** - Favoriten-Jobs markieren

### Langfristig (2+ Wochen)
- [ ] **Datenbank** - Historische Daten speichern
- [ ] **Trend-Analyse** - Jobmarkt-Entwicklung über Zeit
- [ ] **Job-Alerts** - Email-Benachrichtigung bei neuen passenden Jobs
- [ ] **ML-Matching** - Automatisches Matching basierend auf eigenem Profil

## 📚 Learnings

Was ich in diesem Projekt gelernt habe:

### APIs & Datenverarbeitung
- ✅ REST API-Calls mit `requests`
- ✅ JSON-Daten parsen und verarbeiten
- ✅ Daten filtern und aggregieren mit Python
- ✅ Umgang mit unstrukturierten Daten

### Web-Development
- ✅ Streamlit Dashboard-Entwicklung
- ✅ Layout mit Columns und Containern
- ✅ Page Config und Styling

### Datenvisualisierung
- ✅ Plotly Express für interaktive Charts
- ✅ Pie Charts erstellen und customizen
- ✅ Dataframes in Streamlit anzeigen

### Best Practices
- ✅ Virtual Environments nutzen
- ✅ Requirements.txt für Dependencies
- ✅ Code-Kommentare und Struktur
- ✅ Git & GitHub Workflow

## 👤 Kontakt

**Nico Ohler**

- 📧 Email: nico.ohler99.no@gmail.com
- 💼 LinkedIn: [Dein LinkedIn Profil]
- 🐙 GitHub: [github.com/DEIN-USERNAME]

## 📝 Lizenz

Dieses Projekt steht unter der MIT License - siehe [LICENSE](LICENSE) Datei für Details.

## 🙏 Acknowledgments

- [RemoteOK](https://remoteok.com/) für die kostenlose API
- [Streamlit](https://streamlit.io/) für das großartige Framework
- [Plotly](https://plotly.com/) für interaktive Visualisierungen

---

⭐ **Wenn dir dieses Projekt gefällt, gib ihm einen Star auf GitHub!**

---

**Erstellt als Portfolio-Projekt im Rahmen meiner Jobsuche im Data/AI-Bereich | Februar 2025**