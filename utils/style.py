import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        /* EGYHIA Theme Colors */
        :root {
            --egyhia-green: #2ecc71;
            --egyhia-dark: #2c3e50;
            --egyhia-blue: #3498db;
            --egyhia-light: #ecf0f1;
        }
        
        .stApp {
            background-color: #f8f9fa;
        }
        
        h1, h2, h3 {
            color: var(--egyhia-dark);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        .stButton>button {
            background-color: var(--egyhia-green);
            color: white;
            border-radius: 5px;
            border: none;
            padding: 10px 24px;
        }
        
        .stButton>button:hover {
            background-color: #27ae60;
            color: white;
        }
        
        .kpi-card {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
            border-top: 4px solid var(--egyhia-green);
            margin-bottom: 20px;
        }
        
        .kpi-title {
            color: var(--egyhia-dark);
            font-size: 1.1rem;
            font-weight: 600;
        }
        
        .kpi-value {
            color: var(--egyhia-blue);
            font-size: 2rem;
            font-weight: bold;
            margin-top: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
