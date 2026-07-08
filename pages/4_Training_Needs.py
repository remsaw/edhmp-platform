import streamlit as st
import pandas as pd
from utils.style import apply_custom_css

st.set_page_config(page_title="Training Needs - EDHMP", page_icon="🎓", layout="wide")
apply_custom_css()

st.title("🎓 Training Needs Matrix")
st.write("Automatically matches identified gaps with tailored training programs for specific staff roles, along with a comprehensive role-based training matrix.")

st.divider()

st.subheader("Role-based Training Matrix")

static_needs_data = {
    "Role": [
        "Top Management", 
        "Physicians", 
        "Nurses", 
        "Pharmacists", 
        "Laboratory", 
        "Radiology", 
        "Medical Records", 
        "Quality", 
        "Statistics", 
        "IT"
    ],
    "Training Needs": [
        "Digital Leadership – Change Management – Digital Governance",
        "EMR Advanced – ICD-11 – Clinical Documentation – AI in Healthcare",
        "Nursing Informatics – EMR – Documentation",
        "Pharmacy Informatics",
        "Laboratory Informatics",
        "RIS – PACS",
        "ICD-11 – Data Quality – Health Records",
        "KPI – Dashboard – Quality Indicators – Power BI",
        "SPSS – Power BI – Excel – Statistics",
        "Cybersecurity – Server – Cloud – Networking"
    ]
}

static_df = pd.DataFrame(static_needs_data)
st.table(static_df)

st.divider()

st.subheader("Interactive Training Matrix")

matrix_data = [
    {"Department": "Top Management", "Specialty": "Management", "Program": "Digital Leadership", "Priority": "High", "Duration": "2 Days"},
    {"Department": "Physicians", "Specialty": "Clinical", "Program": "AI in Healthcare", "Priority": "Medium", "Duration": "3 Days"},
    {"Department": "Physicians", "Specialty": "Clinical", "Program": "EMR Advanced", "Priority": "High", "Duration": "2 Days"},
    {"Department": "Nurses", "Specialty": "Clinical", "Program": "Nursing Informatics", "Priority": "High", "Duration": "3 Days"},
    {"Department": "Medical Records", "Specialty": "Admin", "Program": "ICD-11", "Priority": "Critical", "Duration": "4 Days"},
    {"Department": "Quality", "Specialty": "Analytics", "Program": "Power BI & Dashboards", "Priority": "Critical", "Duration": "5 Days"},
    {"Department": "IT", "Specialty": "Tech", "Program": "Cybersecurity", "Priority": "Critical", "Duration": "4 Days"},
    {"Department": "Statistics", "Specialty": "Analytics", "Program": "SPSS & Advanced Statistics", "Priority": "Medium", "Duration": "5 Days"}
]

matrix_df = pd.DataFrame(matrix_data)

col1, col2, col3 = st.columns(3)
with col1:
    dept_filter = st.multiselect("Filter by Department", options=matrix_df['Department'].unique())
with col2:
    spec_filter = st.multiselect("Filter by Specialty", options=matrix_df['Specialty'].unique())
with col3:
    prio_filter = st.multiselect("Filter by Priority", options=matrix_df['Priority'].unique())

filtered_df = matrix_df.copy()
if dept_filter:
    filtered_df = filtered_df[filtered_df['Department'].isin(dept_filter)]
if spec_filter:
    filtered_df = filtered_df[filtered_df['Specialty'].isin(spec_filter)]
if prio_filter:
    filtered_df = filtered_df[filtered_df['Priority'].isin(prio_filter)]

st.dataframe(filtered_df, use_container_width=True)
