# 💼 Data & AI Jobs Dashboard

An interactive Streamlit dashboard for visualizing and analyzing Data and AI job listings fetched from the RemoteOK API.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📋 Table of Contents

- [About the project](#about-the-procekt)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Project Structure](#projekt-structure)
- [API Information](#api-information)
- [License](#license)

## 🎯 About the Project

This project is an **interactive dashboard** designed to explore the Data and AI job market. It uses the RemoteOK API to fetch current remote job listings, filters them by relevant keywords, and visualizes the results in a clear and user-friendly way.

## ✨ Features

- 🔍 **Automatic Filtering** - Identifies Data/AI-relevant jobs from 95+ remote positions
- 📊 **Interactive Visualizations** - Pie chart showing top job categories
- 📋 **Clean Job Table** - All filtered jobs at a glance
- 📈 **Key Metrics** - Quick overview of total and filtered job counts
- 🔄 **Live-Daten** - Updates on every page load
- 💻 **Responsive Design** - Wide layout for improved readability

## 🖼️ Demo

### Dashboard-Ansicht
![Overview](data-ai-dashboard-overview.png)

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python Package Manager)
- Git (optional)

### Step-by-Step Guide

1. **Clone the repository** (or download as ZIP):
   ```bash
   git clone https://github.com/Ni-o-iN/data-jobs-dashboard.git
   cd data-jobs-dashboard
   ```

2. **Create a virtual environment** (recommended):
   
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

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the dashboard:**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser:**
   - The dashboard will open automatically at `http://localhost:8501`
   - If not, open the link manually in your browser

## 💡 Usage

### Dashboard Components

1. **Key Metrics (Top Section)**
   - Displays the total number of jobs
   - Shows the number of filtered Data/AI jobs

2. **Top 10 Job Categories (Pie Chart)**
   - Visualizes the most common tags in Data/AI jobs
   - Interactive: hover to see details

3. **Job Table**
   - Lists all filtered jobs with position, company, location, and tags
   - Scrollable for large result sets
   - Sortable by clicking on column headers

### Filter Keywords

The dashboard filters jobs using the following keywords:
- `data`
- `ai`
- `machine learning`
- `ml`

Jobs are included if these keywords appear in:
- the job title / position
- the tags

## 🛠️ Technologies

| Technology | Usage |
|------------|-----------|
| **Python 3.10+** | Programming language |
| **Streamlit 1.30.0+** | Web dashboard framework |
| **Plotly Express** | Interactive visualizations |
| **Requests** | API calls |
| **Collections (Counter)** | Data aggregation |

## 📁 Projekt Structure

```
data-jobs-dashboard/
│
├── app.py                          # Main dashboard application
├── requirements.txt                # Python dependencies
└── data-ai-dashboard-overview.png  # Dashboard Overview
```

## 🌐 API Information

### RemoteOK API

- **Endpoint:** `https://remoteok.com/api`
- **Type:** REST API
- **Authentication:** None (public)
- **Rate Limit:** Fair Use (please dont spam)
- **Data Format:** JSON

**Example response::**
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

**Note:** The API primarily provides job categories as tags (e.g. “engineer”, “senior”) rather than specific technical skills (e.g. “python”, “pandas”).

## 📝 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
