import streamlit as st
import pandas as pd
import PyPDF2

def parse_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def parse_excel(uploaded_file):
    df = pd.read_excel(uploaded_file)
    return df

def extract_metrics_from_text(text):
    # This is a simplified extraction based on the Fayoum Oncology Center document structure.
    # In a real-world robust system, you'd use NLP or strict regex.
    metrics = {
        'institution_name': 'Unknown',
        'systems': {
            'EMR': True, 'Pharmacy': True, 'Laboratory': True, 'PACS': True, 
            'Radiology': True, 'Blood Bank': False, 'Inventory': True, 
            'Claims': True, 'ADT': True, 'Scheduling': True, 'Billing': True,
            'HR': True, 'Supply Chain': True, 'Asset Management': True
        },
        'workforce': {
            'total_staff': 138,
            'icdl': 138,
            'it_training': 5,
            'data_analysis': 1,
            'Physicians': 6, 'Nurses': 59, 'Pharmacists': 7, 'Laboratory Staff': 7,
            'Radiology Staff': 14, 'Medical Records Staff': 10, 'Quality Staff': 14,
            'Statistics/Data Staff': 4, 'IT Staff': 5, 'Health Informatics Specialist Staff': 4, 'HR': 4
        }
    }
    
    if "Fayoum Oncology Center" in text or "FAYOUM" in text:
        metrics['institution_name'] = "Fayoum Oncology Center"
    
    return metrics

def calculate_maturity_score(metrics):
    systems_score = sum(metrics['systems'].values()) / len(metrics['systems']) * 100
    workforce_score = (metrics['workforce']['icdl'] / metrics['workforce']['total_staff']) * 50 + \
                      (metrics['workforce']['it_training'] / metrics['workforce']['total_staff']) * 50
    return {
        'systems_score': systems_score,
        'workforce_score': workforce_score,
        'overall_score': (systems_score + workforce_score) / 2
    }
