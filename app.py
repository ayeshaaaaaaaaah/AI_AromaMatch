import streamlit as st
import pandas as pd

st.set_page_config(page_title="AromaMatch AI Platform", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=Montserrat:wght@300;400;500&display=swap');
    
    .stApp {
        background-color: #fcfbfc;
    }
    
    h1, h2, h3 {
        font-family: 'Cinzel', serif !important;
        letter-spacing: 1.5px;
        color: #1a1a1a !important;
    }
    
    div, p, span, label {
        font-family: 'Montserrat', sans-serif !important;
    }
    
    .hero-container {
        background: linear-gradient(135deg, #111111 0%, #2c2523 100%);
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 35px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        border: 1px solid #d4af37;
    }
    
    .hero-title {
        color: #ffffff !important;
        font-size: 38px !important;
        font-weight: 600 !important;
        margin-bottom: 8px !important;
        text-transform: uppercase;
    }
    
    .hero-subtitle {
        color: #d4af37 !important;
        font-size: 16px !important;
        letter-spacing: 3px;
        text-transform: uppercase;
        font-weight: 400;
        margin-bottom: 0px !important;
    }
    
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #eaeaea;
        padding: 20px 25px !important;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.02);
        transition: all 0.3s ease;
    }
    
    div[data-testid="stMetric"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(212,175,55,0.08);
        border-color: #d4af37;
    }
    
    div[data-testid="stMetricLabel"] p {
        font-size: 11px !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        color: #8c8c8c !important;
        font-weight: 500 !important;
    }
    
    div[data-testid="stMetricValue"] div {
        font-size: 20px !important;
        font-weight: 500 !important;
        color: #1a1a1a !important;
    }
    
    div.stButton > button {
        background: linear-gradient(135deg, #2c2523 0%, #111111 100%) !important;
        color: #d4af37 !important;
        border: 1px solid #d4af37 !important;
        padding: 12px 35px !important;
        font-family: 'Cinzel', serif !important;
        font-size: 15px !important;
        letter-spacing: 2px !important;
        border-radius: 8px !important;
        transition: all 0.4s ease !important;
        width: auto !important;
        margin: 20px auto !important;
        display: block !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
    }
    
    div.stButton > button:hover {
        color: #ffffff !important;
        background: linear-gradient(135deg, #d4af37 0%, #aa841c 100%) !important;
        border-color: #ffffff !important;
        box-shadow: 0 6px 20px rgba(212,175,55,0.3) !important;
        transform: translateY(-2px);
    }
    
    .rec-card {
        background-color: #ffffff;
        border: 1px solid #f0edf0;
        padding: 24px;
        border-radius: 14px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.02);
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        height: 100%;
    }
    
    .rec-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 28px rgba(0,0,0,0.07);
        border-color: #d4af37;
    }
    
    .rec-title {
        font-family: 'Cinzel', serif !important;
        font-size: 18px !important;
        color: #111111 !important;
        margin-top: 0 !important;
        margin-bottom: 15px !important;
        font-weight: 600;
        line-height: 1.3;
        min-height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .rec-divider {
        height: 1px;
        background: linear-gradient(to right, transparent, #d4af37, transparent);
        margin: 12px 0;
    }
    
    .rec-meta {
        font-size: 13px !important;
        color: #555555 !important;
        margin: 6px 0 !important;
    }
    
    .rec-meta b {
        color: #9c847c !important;
        font-weight: 500;
        text-transform: uppercase;
        font-size: 11px;
        letter-spacing: 1px;
    }
    
    .rec-cluster {
        font-size: 11px !important;
        font-weight: 500 !important;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #aa841c !important;
        margin-top: 15px !important;
        margin-bottom: 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_fast_data():
    df = pd.read_csv(r'C:\Users\MADINA COMPUTERS\Downloads\Perfumes_dataset.csv')
    df.columns = df.columns.str.strip().str.lower()
    
    column_mappings = {
        'perfume': ['perfume', 'name', 'title', 'fragrance'],
        'brand': ['brand', 'company', 'make'],
        'scent_category': ['scent_category', 'category', 'notes', 'scent'],
        'target_class': ['target_class', 'gender', 'target', 'audience']
    }
    
    for standard_name, options in column_mappings.items():
        for opt in options:
            if opt in df.columns and standard_name not in df.columns:
                df = df.rename(columns={opt: standard_name})
                break
              
    for col in ['perfume', 'brand', 'scent_category', 'target_class']:
        if col not in df.columns:
            df[col] = ''

    df = df.dropna(subset=['perfume']).reset_index(drop=True)
    df = df.fillna('')
    
    if 'cluster_id' not in df.columns:
        df['cluster_id'] = 0
        
    return df

df = load_fast_data()

st.markdown("""
    <div class="hero-container">
        <div class="hero-title">AromaMatch</div>
        <div class="hero-subtitle">Recommendation System</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<h3 style='font-size: 18px; margin-bottom: 10px; color: #444;'>Select Olfactory Signature</h3>", unsafe_allow_html=True)
target_perfume = st.selectbox("Select Olfactory Signature", df['perfume'].unique(), label_visibility="collapsed")

target_row = df[df['perfume'] == target_perfume].iloc[0]

t_brand = str(target_row['brand']).strip()
t_cat = str(target_row['scent_category']).strip()
t_target = str(target_row['target_class']).strip()

if t_brand in ['', 'unknown', 'Unknown']: t_brand = 'Universal Baseline'
if t_cat in ['', 'unknown', 'Unknown']: t_cat = 'Signature Blend'
if t_target in ['', 'unknown', 'Unknown']: t_target = 'Unisex'

st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Brand Baseline", t_brand)
col2.metric("Scent Category", t_cat)
col3.metric("Target Class", t_target)
col4.metric("Concentration", "EDP")
col5.metric("Scent Group", f"Cluster {int(target_row['cluster_id']) + 1}")

st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

if st.button("Discover Curated Matches"):
    st.markdown("<h3 style='text-align: center; margin-top: 20px; margin-bottom: 30px;'>Exquisite Curated Matches</h3>", unsafe_allow_html=True)
    
    recommendations = df[(df['scent_category'] == target_row['scent_category']) & (df['perfume'] != target_perfume)].head(5)
    
    if len(recommendations) < 5:
        recommendations = df[df['perfume'] != target_perfume].head(5)

    cols = st.columns(5)
    for col, (_, rec) in zip(cols, recommendations.iterrows()):
        rec_brand = str(rec['brand']).strip()
        rec_cat = str(rec['scent_category']).strip()
        rec_target = str(rec['target_class']).strip()
        
        if rec_brand in ['', 'unknown', 'Unknown']: rec_brand = 'Premium'
        if rec_cat in ['', 'unknown', 'Unknown']: rec_cat = 'Signature Blend'
        if rec_target in ['', 'unknown', 'Unknown']: rec_target = 'Unisex'
        
        with col:
            st.markdown(f"""
            <div class="rec-card">
                <div class="rec-title">{rec['perfume']}</div>
                <div class="rec-divider"></div>
                <p class="rec-meta"><b>Brand</b><br>{rec_brand}</p>
                <p class="rec-meta"><b>Category</b><br>{rec_cat}</p>
                <p class="rec-meta"><b>Target</b><br>{rec_target}</p>
                <p class="rec-cluster">Cluster {int(rec['cluster_id']) + 1}</p>
            </div>
            """, unsafe_allow_html=True)