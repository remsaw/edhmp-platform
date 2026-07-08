import streamlit as st
from utils.style import apply_custom_css
from utils.data_parser import parse_pdf, parse_excel, extract_metrics_from_text, calculate_maturity_score

st.set_page_config(
    page_title="EDHMP - EGYHIA Digital Health Maturity Platform",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_css()

# Logo and Title
st.markdown("<h1 style='text-align: center; color: var(--egyhia-dark);'>Egyptian Health Informatics Association</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 4])
with col1:
    st.image("EgYPTIAN HEALTH INFORMATICS ASSOCIATION (3) (1).png", use_container_width=True)
with col2:
    st.title("Digital Health Maturity Platform (EDHMP)")
    st.markdown("Analyze maturity assessment results, extract gaps, and propose professional training programs.")

st.divider()

if 'uploader_key' not in st.session_state:
    st.session_state['uploader_key'] = 0

def reset_dashboard():
    st.session_state['uploader_key'] += 1
    if 'metrics' in st.session_state:
        del st.session_state['metrics']
    if 'scores' in st.session_state:
        del st.session_state['scores']

st.header("1. Upload Assessment Data")
st.write("Please upload the institution's assessment results in PDF or Excel format.")

uploaded_file = st.file_uploader("Upload PDF or Excel file", type=['pdf', 'xlsx'], key=f"uploader_{st.session_state['uploader_key']}")

if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1].lower()
    
    try:
        with st.spinner("Processing document..."):
            if file_type == 'pdf':
                text_content = parse_pdf(uploaded_file)
                metrics = extract_metrics_from_text(text_content)
            elif file_type == 'xlsx':
                # Simplified for this prototype: we assume text extraction logic handles the data
                # In real scenario, we'd map excel columns to metrics directly
                df = parse_excel(uploaded_file)
                # Mocking extraction for demo
                metrics = extract_metrics_from_text("Fayoum Oncology Center")
            
            scores = calculate_maturity_score(metrics)
            
            # Save to session state
            st.session_state['metrics'] = metrics
            st.session_state['scores'] = scores
            
            st.success(f"Successfully processed data for **{metrics['institution_name']}**!")
            
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")

# Display Summary if data is loaded
if 'metrics' in st.session_state:
    metrics = st.session_state['metrics']
    scores = st.session_state['scores']
    
    st.header("2. Quick Overview")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Institution</div>
            <div class="kpi-value" style="font-size: 1.2rem;">{metrics['institution_name']}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Overall Score</div>
            <div class="kpi-value">{scores['overall_score']:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Systems Score</div>
            <div class="kpi-value">{scores['systems_score']:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Workforce Score</div>
            <div class="kpi-value">{scores['workforce_score']:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.info("👈 Navigate to the pages in the sidebar for detailed analysis, gaps, and training recommendations.")
    st.button("🧹 Clear Dashboard & Start Over", on_click=reset_dashboard, type="primary")
else:
    st.info("Upload an assessment file to begin.")
