import streamlit as st
import pandas as pd
from utils.style import apply_custom_css

st.set_page_config(page_title="Gap Analysis - EDHMP", page_icon="🔍", layout="wide")
apply_custom_css()

if 'metrics' not in st.session_state:
    st.warning("Please upload assessment data on the Home page first.")
    st.stop()

metrics = st.session_state['metrics']

st.title("🔍 Gap Analysis")
st.write("Automatically identifies and categorizes gaps into Critical, High, Medium, and Low.")

st.subheader("Gap Summary")
summary_data = {
    "Domain": ["Information Systems", "Infrastructure", "Workforce Skills", "Data Analysis", "Health Informatics"],
    "Status": ["🟢", "🟢", "🔴", "🔴", "🟡"],
    "Priority": ["Low", "Low", "High", "Critical", "Medium"]
}
st.table(pd.DataFrame(summary_data))

st.divider()

gaps = []

# Systems Gaps
sys_df = pd.DataFrame(list(metrics['systems'].items()), columns=['System', 'Implemented'])
missing_systems = sys_df[~sys_df['Implemented']]['System'].tolist()

for sys in missing_systems:
    if sys in ['EMR', 'Laboratory', 'Radiology', 'Pharmacy', 'Blood Bank']:
        gaps.append({"Gap": f"Missing Core Clinical System: {sys}", "Category": "Systems", "Severity": "Critical"})
    else:
        gaps.append({"Gap": f"Missing Administrative System: {sys}", "Category": "Systems", "Severity": "Medium"})

# Workforce Gaps
total = metrics['workforce']['total_staff']
icdl = metrics['workforce']['icdl']
it = metrics['workforce']['it_training']
data = metrics['workforce']['data_analysis']

if (total - icdl) > 0:
    gaps.append({"Gap": f"{total - icdl} staff members lack basic digital literacy (ICDL).", "Category": "Workforce", "Severity": "High"})

if (it / total) < 0.1:
    gaps.append({"Gap": "Severely low number of staff with specialized IT training.", "Category": "Workforce", "Severity": "High"})

if (data / total) < 0.05:
    gaps.append({"Gap": "Almost no staff trained in Data Analysis, limiting insights generation.", "Category": "Workforce", "Severity": "Medium"})

gap_df = pd.DataFrame(gaps)

# Display Gaps
st.subheader("Identified Gaps")

def color_severity(val):
    color = ''
    if val == 'Critical': color = '#e74c3c'
    elif val == 'High': color = '#e67e22'
    elif val == 'Medium': color = '#f1c40f'
    elif val == 'Low': color = '#3498db'
    return f'background-color: {color}; color: white; font-weight: bold;'

if not gap_df.empty:
    st.dataframe(gap_df.style.map(color_severity, subset=['Severity']), use_container_width=True)
else:
    st.success("No significant gaps identified!")
