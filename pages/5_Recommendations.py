import streamlit as st
from utils.style import apply_custom_css

st.set_page_config(page_title="Recommendations - EDHMP", page_icon="💡", layout="wide")
apply_custom_css()

st.title("💡 Strategic Recommendations")
st.write("High-level strategic recommendations categorized by timeframe.")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style='background-color: white; padding: 20px; border-radius: 10px; border-top: 5px solid #e74c3c; box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%;'>
        <h3 style='color: #e74c3c; margin-top: 0;'>🚨 Immediate Actions</h3>
        <ul>
            <li>Address Critical Gaps in Data Analysis</li>
            <li>Launch Basic Cybersecurity Awareness</li>
            <li>Establish Digital Health Governance Committee</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='background-color: white; padding: 20px; border-radius: 10px; border-top: 5px solid #e67e22; box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%;'>
        <h3 style='color: #e67e22; margin-top: 0;'>⚡ Short-term</h3>
        <ul>
            <li>Enroll specialized staff in Power BI & Dashboarding courses</li>
            <li>Assess Blood Bank System requirements</li>
            <li>Improve clinical documentation quality</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='background-color: white; padding: 20px; border-radius: 10px; border-top: 5px solid #f1c40f; box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%;'>
        <h3 style='color: #f1c40f; margin-top: 0;'>📅 Mid-term</h3>
        <ul>
            <li>Implement missing clinical/administrative systems</li>
            <li>Integrate AI in Healthcare for targeted departments</li>
            <li>Advance EMR utilization (CDSS integration)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style='background-color: white; padding: 20px; border-radius: 10px; border-top: 5px solid #2ecc71; box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%;'>
        <h3 style='color: #2ecc71; margin-top: 0;'>🚀 Long-term</h3>
        <ul>
            <li>Achieve full systems interoperability (HL7/FHIR)</li>
            <li>Establish regional digital health leadership</li>
            <li>Continuous Digital Transformation & Innovation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
