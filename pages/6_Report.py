import streamlit as st
from utils.style import apply_custom_css
import datetime
from fpdf import FPDF
import base64

st.set_page_config(page_title="Report - EDHMP", page_icon="📄", layout="wide")
apply_custom_css()

if 'metrics' not in st.session_state:
    st.warning("Please upload assessment data on the Home page first.")
    st.stop()

metrics = st.session_state['metrics']
scores = st.session_state['scores']

st.title("📄 Generate Professional Report")
st.write("Export the complete analysis as a PDF report.")

def generate_pdf(metrics, scores):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="EGYHIA Digital Health Maturity Assessment Report", ln=True, align='C')
    pdf.ln(10)
    
    # Institution Details
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt=f"Institution: {metrics['institution_name']}", ln=True)
    pdf.cell(200, 10, txt=f"Date Generated: {datetime.date.today()}", ln=True)
    pdf.ln(10)
    
    # Executive Summary
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="1. Executive Summary", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.cell(200, 10, txt=f"Overall Digital Maturity Score: {scores['overall_score']:.1f}%", ln=True)
    pdf.cell(200, 10, txt=f"Systems Score: {scores['systems_score']:.1f}%", ln=True)
    pdf.cell(200, 10, txt=f"Workforce Score: {scores['workforce_score']:.1f}%", ln=True)
    pdf.ln(5)
    
    # Key Findings & Gaps
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="2. Key Findings & Identified Gaps", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, txt="- High adoption of core clinical systems. Most systems are implemented.")
    pdf.multi_cell(0, 10, txt="- Excellent basic digital literacy among staff.")
    pdf.multi_cell(0, 10, txt="- Critical Gap: Missing specific systems like Blood Bank.")
    pdf.multi_cell(0, 10, txt="- Critical Gap: Lack of specialized IT and Data Analysis skills across departments.")
    pdf.ln(5)
    
    # Strategic Recommendations
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="3. Strategic Recommendations", ln=True)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Immediate Actions:", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, txt="Address Critical Gaps in Data Analysis, Launch Basic Cybersecurity Awareness, Establish Digital Health Governance Committee.")
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Short-term:", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, txt="Enroll specialized staff in Power BI courses, Assess Blood Bank System requirements.")
    pdf.ln(5)
    
    # Training Plan
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="4. Training Plan Matrix", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, txt="- Top Management: Digital Leadership, Change Management (Priority: High)")
    pdf.multi_cell(0, 10, txt="- IT Staff: Cybersecurity, Server, Cloud (Priority: Critical)")
    pdf.multi_cell(0, 10, txt="- Quality & Statistics: Advanced Healthcare Data Analytics, Power BI (Priority: Critical)")
    pdf.multi_cell(0, 10, txt="- Physicians/Nurses: EMR Advanced, Clinical Documentation (Priority: High)")
    
    # Output PDF to byte string
    return pdf.output(dest='S').encode('latin-1')

if st.button("Generate PDF Report", type="primary"):
    with st.spinner("Compiling PDF report..."):
        try:
            pdf_bytes = generate_pdf(metrics, scores)
            st.success("PDF Report generated successfully!")
            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_bytes,
                file_name=f"{metrics['institution_name'].replace(' ', '_')}_Report.pdf",
                mime="application/pdf"
            )
        except Exception as e:
            st.error(f"Error generating PDF: {str(e)}")
