import streamlit as st
from utils.style import apply_custom_css

st.set_page_config(page_title="Admin - EDHMP", page_icon="⚙️", layout="wide")
apply_custom_css()

st.title("⚙️ Admin Settings")
st.write("Configure platform settings and manage users.")

st.warning("Admin dashboard is currently under construction for the beta version.")

st.markdown("""
### Planned Features:
- User Access Control (Role-based access)
- Assessment Template Customization
- Global Analytics (Compare multiple institutions)
- Training Course Catalog Management
""")
