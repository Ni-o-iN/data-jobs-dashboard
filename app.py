import streamlit as st
import requests
import plotly.express as px
from collections import Counter

#API request
url = "https://remoteok.com/api"
response = requests.get(url)
data = response.json()

print(f"Anzahl aller Jobs: {len(data)}")

data_ai_keywords = ["data", "ai", "machine learning", "ml"]

filtered_jobs = []

for job in data:
    tags = job.get("tags", [])
    tags_string = " ".join(tags).lower()
    position = str(job.get("position", "")).lower()

    for keyword in data_ai_keywords:
        if keyword in tags_string or keyword in position:
            filtered_jobs.append(job)
            break

print(f"Anzahl passender Jobs {len(filtered_jobs)}")
#print(filtered_jobs[1])

all_tags = []
for job in filtered_jobs:
    tags = job.get("tags", [])
    all_tags.extend(tags)

tag_counts = Counter(all_tags)
top_10_tags = tag_counts.most_common(10)



#-----Streamlit Anwenung-----

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>Data AI Jobs Dashboard</h1>", unsafe_allow_html=True)

st.markdown("---")

# Key Metrics
col1, col2, col3, col4 = st.columns([2.5,1,2,1])
with col2:
    st.metric("Gesamt Jobs", len(data))
with col3:
    st.metric("Data/AI Jobs", len(filtered_jobs))

st.markdown("---")

# Pie Chart für Top Tags
st.subheader("🏷️ Top 10 Job-Kategorien")

# Daten vorbereiten für Plotly
labels = [tag for tag, count in top_10_tags]
values = [count for tag, count in top_10_tags]

fig = px.pie(
    names=labels,
    values=values,
    title="Häufigste Tags in Data/AI Jobs"
)

st.plotly_chart(fig)

# Jobs Tabelle
st.subheader("📋 Gefundene Jobs")

job_data = []
for job in filtered_jobs:
    job_data.append({
        "Position": job.get("position", "N/A"),
        "Company": job.get("company", "N/A"),
        "Location": job.get("location", "N/A"),
        "Tags": ", ".join(job.get("tags", [])[:5])
    })

st.dataframe(job_data, hide_index=False)