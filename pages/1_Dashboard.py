import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from utils.style import apply_custom_css

st.set_page_config(page_title="Dashboard - EDHMP", page_icon="📊", layout="wide")
apply_custom_css()

if 'metrics' not in st.session_state:
    st.warning("Please upload assessment data on the Home page first.")
    st.stop()

metrics = st.session_state['metrics']
scores = st.session_state['scores']

st.title("📊 Executive Dashboard")
st.markdown("### Digital Maturity Level")

# Maturity Level calculation
maturity_level = "Beginner"
if scores['overall_score'] > 80:
    maturity_level = "Advanced"
elif scores['overall_score'] > 50:
    maturity_level = "Intermediate"

st.success(f"**Current Maturity Level:** {maturity_level}")

col1, col2 = st.columns(2)

with col1:
    # Gauge Chart
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = scores['overall_score'],
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Overall Maturity Score", 'font': {'size': 24, 'color': '#2c3e50'}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#2ecc71"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 50], 'color': '#e74c3c'},
                {'range': [50, 80], 'color': '#f1c40f'},
                {'range': [80, 100], 'color': '#2ecc71'}],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': scores['overall_score']}
        }
    ))
    st.plotly_chart(fig_gauge, use_container_width=True)

with col2:
    # Radar Chart
    categories = ['Information Systems', 'Workforce', 'Infrastructure', 'Data Quality', 'Cybersecurity']
    # Mocking missing scores based on the overall to show a complete radar
    values = [scores['systems_score'], scores['workforce_score'], 90, 85, 100]
    
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Maturity',
        line_color='#3498db'
    ))
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100])
        ),
        showlegend=False,
        title="Maturity Dimensions"
    )
    st.plotly_chart(fig_radar, use_container_width=True)

st.divider()

st.header("💻 Information Systems Dashboard")
sys_df = pd.DataFrame(list(metrics['systems'].items()), columns=['System', 'Implemented'])

col_sys1, col_sys2 = st.columns([1, 2])

with col_sys1:
    # Donut Chart for systems
    implemented_count = sys_df['Implemented'].sum()
    missing_count = len(sys_df) - implemented_count
    
    fig_donut = px.pie(
        names=['Implemented', 'Missing'], 
        values=[implemented_count, missing_count],
        hole=0.5,
        color=['Implemented', 'Missing'],
        color_discrete_map={'Implemented': '#2ecc71', 'Missing': '#e74c3c'},
        title="Systems Implementation Ratio"
    )
    st.plotly_chart(fig_donut, use_container_width=True)

with col_sys2:
    st.subheader("System Status List")
    # Custom display for systems
    implemented_html = "".join([f"<span style='background-color: #2ecc71; color: white; padding: 5px 10px; border-radius: 15px; margin: 5px; display: inline-block;'>✅ {sys}</span>" for sys in sys_df[sys_df['Implemented']]['System']])
    missing_html = "".join([f"<span style='background-color: #e74c3c; color: white; padding: 5px 10px; border-radius: 15px; margin: 5px; display: inline-block;'>❌ {sys}</span>" for sys in sys_df[~sys_df['Implemented']]['System']])
    
    st.markdown("#### ✅ Implemented Systems")
    st.markdown(implemented_html, unsafe_allow_html=True)
    st.markdown("#### ❌ Missing Systems")
    st.markdown(missing_html, unsafe_allow_html=True)
