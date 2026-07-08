import streamlit as st
import plotly.express as px
import pandas as pd
from utils.style import apply_custom_css

st.set_page_config(page_title="Workforce - EDHMP", page_icon="👥", layout="wide")
apply_custom_css()

if 'metrics' not in st.session_state:
    st.warning("Please upload assessment data on the Home page first.")
    st.stop()

metrics = st.session_state['metrics']
wf = metrics['workforce']

st.title("👥 Workforce Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("Total Staff", wf['total_staff'])
col2.metric("ICDL Certified", wf['icdl'], f"{(wf['icdl']/wf['total_staff'])*100:.1f}%")
col3.metric("IT & Data Trained", wf['it_training'] + wf['data_analysis'])

st.divider()

col_dist, col_heat = st.columns(2)

# Roles distribution
roles = {k: v for k, v in wf.items() if k not in ['total_staff', 'icdl', 'it_training', 'data_analysis']}
roles_df = pd.DataFrame(list(roles.items()), columns=['Role', 'Count'])

with col_dist:
    st.subheader("Staff Distribution")
    fig_roles = px.bar(roles_df, x='Role', y='Count', color='Count', color_continuous_scale='Greens')
    st.plotly_chart(fig_roles, use_container_width=True)

with col_heat:
    st.subheader("Digital Skills Heatmap")
    # Mock data for heatmap based on roles
    heatmap_data = pd.DataFrame({
        'Basic Literacy': [100, 100, 100, 100, 100],
        'Advanced IT': [10, 5, 2, 80, 50],
        'Data Analysis': [5, 2, 1, 30, 80]
    }, index=['Physicians', 'Nurses', 'Admin', 'IT', 'Data Staff'])
    
    fig_heat = px.imshow(heatmap_data, text_auto=True, color_continuous_scale='Blues')
    st.plotly_chart(fig_heat, use_container_width=True)
