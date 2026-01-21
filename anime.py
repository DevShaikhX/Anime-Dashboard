import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# ╔════════════════════════════════════════════════════════════════════════════════╗
# ║              ANIME NEXUS - ADVANCED INTELLIGENCE & ANALYTICS PLATFORM              ║
# ║                   "Advancing Human Civilization Through Data"                  ║
# ╚════════════════════════════════════════════════════════════════════════════════╝

# Page configuration
st.set_page_config(
    page_title="🚀 ANIME NEXUS - Mission Control",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════════════════════════════════════════════
# NEXUS DESIGN SYSTEM - FUTURISTIC & CUTTING-EDGE COLORS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <style>
        /* MAIN BACKGROUND - Space/Black aesthetic */
        * {
            font-family: 'Courier New', monospace;
        }
        
        .main {
            background: linear-gradient(135deg, #000000 0%, #0d1b2a 50%, #001a33 100%);
            color: #e8f4f8;
            padding: 0;
        }
        
        .stApp {
            background: linear-gradient(135deg, #000000 0%, #0d1b2a 50%, #001a33 100%);
        }
        
        /* HEADERS - Tesla Red & Cyan Neon */
        h1 {
            background: linear-gradient(90deg, #ff3333 0%, #00d9ff 50%, #ff3333 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 900;
            text-shadow: 0 0 30px rgba(255, 51, 51, 0.5), 0 0 60px rgba(0, 217, 255, 0.3);
            letter-spacing: 3px;
            font-size: 3.5em;
            text-transform: uppercase;
        }
        
        h2 {
            color: #00ff88;
            font-weight: 800;
            text-shadow: 0 0 15px #00ff88, 0 0 30px rgba(0, 255, 136, 0.3);
            letter-spacing: 2px;
            text-transform: uppercase;
            border-bottom: 2px solid #ff3333;
            padding-bottom: 10px;
        }
        
        h3 {
            color: #00d9ff;
            font-weight: 700;
            text-shadow: 0 0 10px #00d9ff;
            letter-spacing: 1px;
        }
        
        /* SUBHEADERS - CRYSTAL CLEAR */
        .stMarkdown h4 {
            color: #ffff00 !important;
            font-weight: 900 !important;
            font-size: 1.3em !important;
            text-shadow: 0 0 10px #ffff00, 0 0 20px #ff3333, 0 0 30px rgba(255, 51, 51, 0.3) !important;
            letter-spacing: 1.5px !important;
            text-transform: uppercase !important;
            margin-top: 15px !important;
            margin-bottom: 15px !important;
            padding: 10px 15px !important;
            border-left: 4px solid #ff3333 !important;
            background: linear-gradient(90deg, rgba(255, 51, 51, 0.1) 0%, transparent 100%) !important;
        }
        
        /* METRIC CARDS - Tesla Style */
        [data-testid="metric-container"] {
            background: linear-gradient(135deg, rgba(0, 217, 255, 0.08) 0%, rgba(255, 51, 51, 0.05) 100%);
            border: 2px solid #ff3333;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(255, 51, 51, 0.2), inset 0 0 20px rgba(0, 217, 255, 0.05);
        }
        
        /* SIDEBAR - Command Center Style */
        .stSidebar {
            background: linear-gradient(180deg, #0a1428 0%, #0d1f3a 100%);
            border-right: 3px solid #ff3333;
        }
        
        .sidebar .sidebar-content {
            border-right: 3px solid #ff3333;
        }
        
        /* BUTTONS - Tesla Inspired */
        .stButton > button {
            background: linear-gradient(135deg, #ff3333 0%, #00ff88 100%);
            color: #000000;
            border: 2px solid #ff3333;
            font-weight: 800;
            border-radius: 4px;
            box-shadow: 0 0 20px rgba(255, 51, 51, 0.4), 0 0 40px rgba(0, 255, 136, 0.2);
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .stButton > button:hover {
            box-shadow: 0 0 40px rgba(255, 51, 51, 0.8), 0 0 60px rgba(0, 255, 136, 0.5);
            transform: scale(1.08);
            background: linear-gradient(135deg, #ff5555 0%, #00ffaa 100%);
        }
        
        /* TABS - Command Center */
        .stTabs [data-baseweb="tab-list"] button {
            color: #00d9ff;
            border-bottom: 3px solid transparent;
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 1px;
        }
        
        .stTabs [aria-selected="true"] {
            border-bottom-color: #ff3333 !important;
            color: #ff3333 !important;
            text-shadow: 0 0 10px #ff3333;
        }
        
        /* TEXT INPUT & SELECT */
        .stSelectbox label, .stMultiSelect label, .stTextInput label {
            color: #00ff88;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* DIVIDERS */
        hr {
            border: 1px solid #ff3333;
            box-shadow: 0 0 10px rgba(255, 51, 51, 0.3);
        }
        
        /* EXPANDER */
        .streamlit-expanderHeader {
            background: linear-gradient(135deg, rgba(255, 51, 51, 0.1) 0%, rgba(0, 255, 136, 0.05) 100%);
            border: 1px solid #ff3333;
            color: #00d9ff;
            border-radius: 4px;
        }
        
        /* SCROLLBAR */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #001a33;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, #ff3333, #00ff88);
            border-radius: 4px;
        }
        
        /* DATAFRAME */
        [data-testid="dataFrame"] {
            border: 1px solid #00ff88 !important;
            background-color: rgba(0, 217, 255, 0.05) !important;
        }
        
        .dataframe {
            color: #e8f4f8;
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)

# Load data with caching
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('anime.csv')
        df['score'] = pd.to_numeric(df['score'], errors='coerce')
        df['rank'] = pd.to_numeric(df['rank'], errors='coerce')
        df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')
        df['members'] = pd.to_numeric(df['members'], errors='coerce')
        df['episodes'] = pd.to_numeric(df['episodes'], errors='coerce')
        df['start_date'] = pd.to_datetime(df['start_date'], errors='coerce')
        df['end_date'] = pd.to_datetime(df['end_date'], errors='coerce')
        return df
    except Exception as e:
        st.error(f"⚠️ ERROR LOADING DATA: {e}")
        return None

df = load_data()
if df is None:
    st.stop()

# ═══════════════════════════════════════════════════════════════════════════════
# MISSION CONTROL SIDEBAR
# ═══════════════════════════════════════════════════════════════════════════════

st.sidebar.markdown("""
    <div style='text-align: center; margin-bottom: 30px;'>
        <h1 style='color: #ff3333; font-size: 2em; margin: 0; text-shadow: 0 0 20px #ff3333;'>
        🚀 MISSION CONTROL</h1>
        <p style='color: #00ff88; font-weight: bold; letter-spacing: 1px; margin-top: 10px;'>
        ANIME INTELLIGENCE SYSTEM</p>
        <hr style='border: 2px solid #ff3333; margin: 15px 0;'>
    </div>
""", unsafe_allow_html=True)

# Advanced Filters
with st.sidebar.expander("🎯 CONTENT FILTERS", expanded=True):
    genre_filter = st.multiselect(
        "Select Anime Types",
        options=sorted(df['type'].unique()),
        default=sorted(df['type'].unique())[:5],
        key="genre"
    )
    
    score_range = st.slider(
        "QUALITY THRESHOLD",
        min_value=float(df['score'].min()),
        max_value=float(df['score'].max()),
        value=(7.0, 9.5),
        step=0.1
    )
    
    members_range = st.slider(
        "MINIMUM AUDIENCE SIZE",
        min_value=0,
        max_value=int(df['members'].max()),
        value=10000,
        step=10000
    )

# System Status
with st.sidebar.expander("� SYSTEM STATUS - LIVE MONITOR", expanded=True):
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(0, 255, 136, 0.2) 0%, rgba(0, 217, 255, 0.1) 100%); 
                border: 2px solid #00ff88; border-radius: 8px; padding: 15px; margin: 10px 0;'>
        <p style='color: #00ff88; font-weight: 900; font-size: 1.1em; text-shadow: 0 0 10px #00ff88; 
                  margin: 8px 0; letter-spacing: 1px; text-transform: uppercase;'>
        📡 Database Status: <span style="color: #ffff00; text-shadow: 0 0 8px #ffff00;">✅ ONLINE</span></p>
        <p style='color: #00d9ff; font-weight: 700; font-size: 1em; margin: 8px 0; letter-spacing: 0.5px;'>
        📊 Total Records: <span style="color: #ffff00; font-weight: 900;">{}</span></p>
        <p style='color: #00d9ff; font-weight: 700; font-size: 1em; margin: 8px 0; letter-spacing: 0.5px;'>
        📅 Latest Update: <span style="color: #ffff00; font-weight: 900;">2026-01-21</span></p>
        <p style='color: #00ff88; font-weight: 700; font-size: 1em; margin: 8px 0; letter-spacing: 0.5px;'>
        💚 System Health: <span style="color: #00ff88; text-shadow: 0 0 8px #00ff88; font-weight: 900; font-size: 1.1em;">99.9%</span></p>
    </div>
    """.format(f"{len(df):,}"), unsafe_allow_html=True)

# Filter data
filtered_df = df[
    (df['type'].isin(genre_filter)) &
    (df['score'] >= score_range[0]) &
    (df['score'] <= score_range[1]) &
    (df['members'] >= members_range)
].dropna(subset=['score', 'rank'])

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN DASHBOARD HEADER
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='text-align: center; margin: 40px 0 30px 0; background: linear-gradient(135deg, rgba(255, 51, 51, 0.15) 0%, rgba(0, 217, 255, 0.1) 100%); 
                padding: 30px; border-radius: 15px; border: 3px solid #ff3333; box-shadow: 0 0 40px rgba(255, 51, 51, 0.3), 0 0 80px rgba(0, 217, 255, 0.15);'>
        <h1 style='font-size: 4em; margin: 0; animation: glow 2s ease-in-out infinite;'>🚀 ANIME NEXUS 🚀</h1>
        <p style='color: #00ff88; font-size: 1.4em; font-weight: bold; 
                  text-shadow: 0 0 15px #00ff88, 0 0 30px rgba(0, 255, 136, 0.3); letter-spacing: 3px; margin-top: 15px;'>
        ⚡ NEXT-GEN ENTERTAINMENT ANALYTICS ⚡</p>
        <p style='color: #00d9ff; font-size: 1.05em; margin-top: 10px; letter-spacing: 1px;
                  text-shadow: 0 0 10px #00d9ff;'>
        "Powering the Future of Anime Intelligence"</p>
        <div style='margin-top: 15px; padding-top: 15px; border-top: 2px solid #ff3333;'>
        <span style='color: #ffff00; font-weight: 900; font-size: 1em; text-shadow: 0 0 10px #ffff00; letter-spacing: 1px;'>
        🚀 ADVANCED MISSION CONTROL CENTER 🚀</span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# MISSION CRITICAL METRICS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div style='background: linear-gradient(90deg, rgba(255, 51, 51, 0.2) 0%, transparent 100%); padding: 15px; border-left: 5px solid #ffff00; border-radius: 5px; margin: 20px 0;'>
<h2 style='color: #ffff00; text-shadow: 0 0 15px #ffff00, 0 0 30px #ff3333; font-size: 1.5em; margin: 0; text-transform: uppercase; letter-spacing: 2px;'>🎯 MISSION CRITICAL METRICS</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    avg_score = filtered_df['score'].mean()
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, rgba(255, 215, 0, 0.2) 0%, rgba(255, 51, 51, 0.1) 100%); 
                border: 2px solid #ffd700; padding: 20px; border-radius: 10px; text-align: center;
                box-shadow: 0 0 20px rgba(255, 215, 0, 0.2);'>
        <p style='color: #ffd700; font-size: 0.9em; font-weight: 900; margin: 0; letter-spacing: 1px; text-transform: uppercase;'>⭐ Avg Rating</p>
        <h3 style='color: #ffff00; font-size: 2.2em; margin: 10px 0; text-shadow: 0 0 15px #ffff00;'>{avg_score:.2f}</h3>
        <p style='color: #00ff88; font-size: 0.95em; margin: 5px 0; font-weight: 700;'>{(avg_score/10)*100:.1f}% Quality</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    total_mem = filtered_df['members'].sum() / 1e6
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, rgba(0, 217, 255, 0.2) 0%, rgba(0, 255, 136, 0.1) 100%); 
                border: 2px solid #00d9ff; padding: 20px; border-radius: 10px; text-align: center;
                box-shadow: 0 0 20px rgba(0, 217, 255, 0.2);'>
        <p style='color: #00d9ff; font-size: 0.9em; font-weight: 900; margin: 0; letter-spacing: 1px; text-transform: uppercase;'>👥 Total Audience</p>
        <h3 style='color: #00ffff; font-size: 2.2em; margin: 10px 0; text-shadow: 0 0 15px #00ffff;'>{total_mem:.1f}M</h3>
        <p style='color: #00ff88; font-size: 0.95em; margin: 5px 0; font-weight: 700;'>Global Members</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    total_anime = len(filtered_df)
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, rgba(143, 0, 255, 0.2) 0%, rgba(255, 51, 51, 0.1) 100%); 
                border: 2px solid #8f00ff; padding: 20px; border-radius: 10px; text-align: center;
                box-shadow: 0 0 20px rgba(143, 0, 255, 0.2);'>
        <p style='color: #8f00ff; font-size: 0.9em; font-weight: 900; margin: 0; letter-spacing: 1px; text-transform: uppercase;'>🎬 Dataset Size</p>
        <h3 style='color: #ffff00; font-size: 2.2em; margin: 10px 0; text-shadow: 0 0 15px #ffff00;'>{total_anime:,}</h3>
        <p style='color: #00ff88; font-size: 0.95em; margin: 5px 0; font-weight: 700;'>Anime Titles</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    avg_pop = filtered_df['popularity'].mean()
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, rgba(255, 170, 0, 0.2) 0%, rgba(0, 255, 136, 0.1) 100%); 
                border: 2px solid #ffaa00; padding: 20px; border-radius: 10px; text-align: center;
                box-shadow: 0 0 20px rgba(255, 170, 0, 0.2);'>
        <p style='color: #ffaa00; font-size: 0.9em; font-weight: 900; margin: 0; letter-spacing: 1px; text-transform: uppercase;'>🔥 Popularity</p>
        <h3 style='color: #ffff00; font-size: 2.2em; margin: 10px 0; text-shadow: 0 0 15px #ffff00;'>#{avg_pop:.0f}</h3>
        <p style='color: #00ff88; font-size: 0.95em; margin: 5px 0; font-weight: 700;'>Avg Rank</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    avg_eps = filtered_df['episodes'].mean()
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, rgba(0, 255, 255, 0.2) 0%, rgba(255, 51, 51, 0.1) 100%); 
                border: 2px solid #00ffff; padding: 20px; border-radius: 10px; text-align: center;
                box-shadow: 0 0 20px rgba(0, 255, 255, 0.2);'>
        <p style='color: #00ffff; font-size: 0.9em; font-weight: 900; margin: 0; letter-spacing: 1px; text-transform: uppercase;'>📺 Episodes</p>
        <h3 style='color: #ffff00; font-size: 2.2em; margin: 10px 0; text-shadow: 0 0 15px #ffff00;'>{avg_eps:.0f}</h3>
        <p style='color: #00ff88; font-size: 0.95em; margin: 5px 0; font-weight: 700;'>Avg Length</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# ELITE RANKING SYSTEM
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div style='background: linear-gradient(90deg, rgba(0, 255, 136, 0.2) 0%, transparent 100%); padding: 15px; border-left: 5px solid #00ff88; border-radius: 5px; margin: 20px 0;'>
<h2 style='color: #00ff88; text-shadow: 0 0 15px #00ff88, 0 0 30px #00ff88; font-size: 1.5em; margin: 0; text-transform: uppercase; letter-spacing: 2px;'>🏆 ELITE RANKING SYSTEM</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style='background: linear-gradient(90deg, rgba(255, 215, 0, 0.15) 0%, transparent 100%); padding: 12px; border-left: 4px solid #ffd700; border-radius: 4px;'>
    <h3 style='color: #ffd700; text-shadow: 0 0 10px #ffd700; font-size: 1.2em; margin: 0; text-transform: uppercase; letter-spacing: 1px;'>👑 TOP 10 MASTERPIECES</h3>
    </div>
    """, unsafe_allow_html=True)
    top_10 = filtered_df.nlargest(10, 'score')[['title', 'score', 'members']].reset_index(drop=True)
    top_10.index = top_10.index + 1
    
    for idx, row in top_10.iterrows():
        st.write(f"**#{idx}** | {row['title']}")
        st.write(f"   ⭐ {row['score']:.2f} | 👥 {row['members']/1e6:.1f}M")

with col2:
    st.markdown("""
    <div style='background: linear-gradient(90deg, rgba(0, 217, 255, 0.15) 0%, transparent 100%); padding: 12px; border-left: 4px solid #00d9ff; border-radius: 4px;'>
    <h3 style='color: #00d9ff; text-shadow: 0 0 10px #00d9ff; font-size: 1.2em; margin: 0; text-transform: uppercase; letter-spacing: 1px;'>🚀 TRENDING NOW</h3>
    </div>
    """, unsafe_allow_html=True)
    trending = filtered_df.nlargest(10, 'members')[['title', 'members', 'score']].reset_index(drop=True)
    trending.index = trending.index + 1
    
    for idx, row in trending.iterrows():
        st.write(f"**#{idx}** | {row['title']}")
        st.write(f"   ⭐ {row['score']:.2f} | 👥 {row['members']/1e6:.1f}M")

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# ADVANCED ANALYTICS SECTION
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div style='background: linear-gradient(90deg, rgba(255, 170, 0, 0.2) 0%, transparent 100%); padding: 15px; border-left: 5px solid #ffaa00; border-radius: 5px; margin: 20px 0;'>
<h2 style='color: #ffaa00; text-shadow: 0 0 15px #ffaa00, 0 0 30px #ff3333; font-size: 1.5em; margin: 0; text-transform: uppercase; letter-spacing: 2px;'>📊 ADVANCED ANALYTICS</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Chart 1: Score Distribution (Tesla Red)
with col1:
    fig1 = px.histogram(
        filtered_df,
        x='score',
        nbins=40,
        color_discrete_sequence=['#ff3333'],
        title='QUALITY DISTRIBUTION MATRIX'
    )
    fig1.update_layout(
        height=400,
        paper_bgcolor='rgba(0, 0, 0, 0.5)',
        plot_bgcolor='rgba(13, 27, 42, 0.5)',
        font=dict(color='#e8f4f8', size=11, family='Courier New'),
        title=dict(font=dict(color='#ff3333', size=15)),
        xaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(255, 51, 51, 0.1)', title='SCORE'),
        yaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(0, 255, 136, 0.1)', title='COUNT'),
        hovermode='x unified'
    )
    st.plotly_chart(fig1, width='stretch')

# Chart 2: Type Distribution (Green/Cyan)
with col2:
    type_dist = filtered_df['type'].value_counts()
    colors_neon = ['#ff3333', '#00ff88', '#00d9ff', '#ffaa00', '#8f00ff', '#ff00ff', '#00ffff']
    
    fig2 = px.pie(
        values=type_dist.values,
        names=type_dist.index,
        title='CONTENT TYPE DISTRIBUTION',
        color_discrete_sequence=colors_neon
    )
    fig2.update_layout(
        height=400,
        paper_bgcolor='rgba(0, 0, 0, 0.5)',
        font=dict(color='#e8f4f8', size=11, family='Courier New'),
        title=dict(font=dict(color='#00ff88', size=15))
    )
    fig2.update_traces(textposition='auto', textfont=dict(color='#000000', size=11, family='Courier New'))
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# CORRELATION ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div style='background: linear-gradient(90deg, rgba(0, 255, 255, 0.2) 0%, transparent 100%); padding: 15px; border-left: 5px solid #00ffff; border-radius: 5px; margin: 20px 0;'>
<h2 style='color: #00ffff; text-shadow: 0 0 15px #00ffff, 0 0 30px #00d9ff; font-size: 1.5em; margin: 0; text-transform: uppercase; letter-spacing: 2px;'>💎 CORRELATION ANALYSIS</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Chart 3: Score vs Members
with col1:
    scatter_df = filtered_df.dropna(subset=['episodes', 'score', 'members'])
    if len(scatter_df) > 0:
        # Replace episodes NaN with a default value for sizing
        scatter_df = scatter_df.copy()
        scatter_df['episodes'] = scatter_df['episodes'].fillna(scatter_df['episodes'].median())
        
        fig3 = px.scatter(
            scatter_df,
            x='members',
            y='score',
            color='score',
            size='episodes',
            hover_name='title',
            color_continuous_scale=['#ff3333', '#00d9ff', '#00ff88'],
            title='POPULARITY-QUALITY CORRELATION',
            size_max=50
        )
        fig3.update_layout(
            height=400,
            paper_bgcolor='rgba(0, 0, 0, 0.5)',
            plot_bgcolor='rgba(13, 27, 42, 0.5)',
            font=dict(color='#e8f4f8', size=11, family='Courier New'),
            title=dict(font=dict(color='#00d9ff', size=15)),
            xaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(0, 255, 136, 0.1)', title='MEMBERS', type='log'),
            yaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(0, 255, 136, 0.1)', title='SCORE'),
            hovermode='closest'
        )
        st.plotly_chart(fig3, width='stretch')

# Chart 4: Episodes vs Score
with col2:
    episodes_score = filtered_df[(filtered_df['episodes'] < 200) & (filtered_df['episodes'].notna()) & (filtered_df['score'].notna())]
    if len(episodes_score) > 0:
        fig4 = px.scatter(
            episodes_score,
            x='episodes',
            y='score',
            color='score',
            hover_name='title',
            color_continuous_scale=['#ff3333', '#ffaa00', '#00ff88'],
            title='LENGTH-QUALITY IMPACT',
            size_max=50
        )
        fig4.update_layout(
            height=400,
            paper_bgcolor='rgba(0, 0, 0, 0.5)',
            plot_bgcolor='rgba(13, 27, 42, 0.5)',
            font=dict(color='#e8f4f8', size=11, family='Courier New'),
            title=dict(font=dict(color='#00ff88', size=15)),
            xaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(0, 255, 136, 0.1)', title='EPISODES'),
            yaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(0, 255, 136, 0.1)', title='SCORE'),
            hovermode='closest'
        )
        st.plotly_chart(fig4, width='stretch')

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# TEMPORAL INTELLIGENCE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div style='background: linear-gradient(90deg, rgba(143, 0, 255, 0.2) 0%, transparent 100%); padding: 15px; border-left: 5px solid #8f00ff; border-radius: 5px; margin: 20px 0;'>
<h2 style='color: #8f00ff; text-shadow: 0 0 15px #8f00ff, 0 0 30px #ff3333; font-size: 1.5em; margin: 0; text-transform: uppercase; letter-spacing: 2px;'>📈 TEMPORAL INTELLIGENCE</h2>
</div>
""", unsafe_allow_html=True)

yearly_data = filtered_df[filtered_df['start_date'].notna()].copy()
yearly_data['year'] = yearly_data['start_date'].dt.year
yearly_data = yearly_data.groupby('year').agg({
    'score': 'mean',
    'members': 'sum',
    'title': 'count'
}).reset_index()
yearly_data.columns = ['Year', 'Avg Score', 'Total Members', 'Count']

if not yearly_data.empty:
    fig5 = make_subplots(
        rows=1, cols=2,
        specs=[[{"secondary_y": False}, {"secondary_y": False}]],
        subplot_titles=("📊 QUALITY EVOLUTION", "📺 PRODUCTION CAPACITY"),
        horizontal_spacing=0.12
    )

    fig5.add_trace(
        go.Scatter(
            x=yearly_data['Year'], 
            y=yearly_data['Avg Score'],
            name='QUALITY SCORE',
            line=dict(color='#00ff88', width=4),
            marker=dict(size=12, color='#ff3333', line=dict(color='#00ff88', width=2)),
            mode='lines+markers'
        ),
        secondary_y=False, row=1, col=1
    )

    fig5.add_trace(
        go.Bar(
            x=yearly_data['Year'], 
            y=yearly_data['Count'],
            name='PRODUCTION COUNT',
            marker_color='#00d9ff',
            opacity=0.7
        ),
        secondary_y=False, row=1, col=2
    )

    fig5.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0, 255, 136, 0.1)', row=1, col=1)
    fig5.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0, 255, 136, 0.1)', row=1, col=2)
    fig5.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0, 255, 136, 0.1)', row=1, col=1)
    fig5.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0, 255, 136, 0.1)', row=1, col=2)

    fig5.update_layout(
        height=450,
        paper_bgcolor='rgba(0, 0, 0, 0.5)',
        plot_bgcolor='rgba(13, 27, 42, 0.5)',
        font=dict(color='#e8f4f8', size=11, family='Courier New'),
        title=dict(text="MARKET EVOLUTION ANALYSIS", font=dict(color='#ff3333', size=16)),
        hovermode='x unified',
        showlegend=True,
        legend=dict(font=dict(color='#e8f4f8'))
    )
    st.plotly_chart(fig5, width='stretch')

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# CATEGORY INTELLIGENCE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div style='background: linear-gradient(90deg, rgba(255, 51, 51, 0.2) 0%, transparent 100%); padding: 15px; border-left: 5px solid #ff3333; border-radius: 5px; margin: 20px 0;'>
<h2 style='color: #ff3333; text-shadow: 0 0 15px #ff3333, 0 0 30px #ffff00; font-size: 1.5em; margin: 0; text-transform: uppercase; letter-spacing: 2px;'>🎯 CATEGORY INTELLIGENCE</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

type_score = filtered_df.groupby('type')['score'].mean().sort_values(ascending=False)
type_members = filtered_df.groupby('type')['members'].sum().sort_values(ascending=False)

with col1:
    if not type_score.empty:
        fig6 = px.bar(
            x=type_score.values,
            y=type_score.index,
            orientation='h',
            color=type_score.values,
            color_continuous_scale=['#ff3333', '#ffaa00', '#00ff88'],
            title='QUALITY BY CATEGORY',
            labels={'x': 'AVERAGE SCORE', 'y': 'CATEGORY'}
        )
        fig6.update_layout(
            height=400,
            paper_bgcolor='rgba(0, 0, 0, 0.5)',
            plot_bgcolor='rgba(13, 27, 42, 0.5)',
            font=dict(color='#e8f4f8', size=11, family='Courier New'),
            title=dict(font=dict(color='#00ff88', size=15)),
            showlegend=False,
            xaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(0, 255, 136, 0.1)'),
            yaxis=dict(showgrid=False)
        )
        st.plotly_chart(fig6, width='stretch')

with col2:
    if not type_members.empty:
        fig7 = px.bar(
            x=type_members.values,
            y=type_members.index,
            orientation='h',
            color=type_members.values,
            color_continuous_scale=['#00d9ff', '#00ff88', '#ff3333'],
            title='AUDIENCE ENGAGEMENT',
            labels={'x': 'TOTAL MEMBERS', 'y': 'CATEGORY'}
        )
        fig7.update_layout(
            height=400,
            paper_bgcolor='rgba(0, 0, 0, 0.5)',
            plot_bgcolor='rgba(13, 27, 42, 0.5)',
            font=dict(color='#e8f4f8', size=11, family='Courier New'),
            title=dict(font=dict(color='#ff3333', size=15)),
            showlegend=False,
            xaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(0, 255, 136, 0.1)'),
            yaxis=dict(showgrid=False)
        )
        st.plotly_chart(fig7, width='stretch')

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# INTELLIGENCE DATABASE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div style='background: linear-gradient(90deg, rgba(0, 255, 136, 0.2) 0%, transparent 100%); padding: 15px; border-left: 5px solid #00ff88; border-radius: 5px; margin: 20px 0;'>
<h2 style='color: #00ff88; text-shadow: 0 0 15px #00ff88, 0 0 30px #00ffff; font-size: 1.5em; margin: 0; text-transform: uppercase; letter-spacing: 2px;'>📡 INTELLIGENCE DATABASE</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    search_term = st.text_input("🔍 SEARCH COMMAND", "", placeholder="Enter anime title...")
with col2:
    sort_by = st.selectbox("SORT BY", ["SCORE (DESC)", "MEMBERS (DESC)", "POPULARITY (ASC)"])

display_cols = ['title', 'score', 'rank', 'type', 'episodes', 'members', 'popularity']
table_df = filtered_df[display_cols].copy()

if search_term:
    table_df = table_df[table_df['title'].str.contains(search_term, case=False, na=False)]

if sort_by == "SCORE (DESC)":
    table_df = table_df.sort_values('score', ascending=False)
elif sort_by == "MEMBERS (DESC)":
    table_df = table_df.sort_values('members', ascending=False)
else:
    table_df = table_df.sort_values('popularity', ascending=True)

st.dataframe(
    table_df.head(50).rename(columns={
        'title': 'TITLE',
        'score': '⭐ SCORE',
        'rank': '🏆 RANK',
        'type': '📺 TYPE',
        'episodes': '📊 EPISODES',
        'members': '👥 MEMBERS',
        'popularity': '🔥 POPULARITY'
    }),
    width='stretch',
    height=400
)

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# SYSTEM FOOTER
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='text-align: center; margin-top: 50px; padding: 30px; 
                background: linear-gradient(135deg, rgba(255, 51, 51, 0.15) 0%, rgba(0, 217, 255, 0.1) 100%);
                border-top: 3px solid #ff3333; border-bottom: 3px solid #ff3333; 
                border-left: 3px solid #00ff88; border-right: 3px solid #00ff88;
                border-radius: 10px; box-shadow: 0 0 40px rgba(255, 51, 51, 0.2);'>
        <p style='color: #ffff00; font-weight: 900; font-size: 1.2em; letter-spacing: 3px; 
                  text-shadow: 0 0 15px #ffff00, 0 0 30px #ff3333; margin: 0;
                  text-transform: uppercase;'>
        🚀 ANIME NEXUS v2026.01 - POWERED BY DEV SHAIKH X 🚀</p>
        <p style='color: #00ff88; font-size: 0.95em; margin-top: 15px; letter-spacing: 1px;
                  text-shadow: 0 0 10px #00ff88; font-weight: 700;'>
        "Making Entertainment Data Transparent & Accessible for Everyone"</p>
        <hr style='border: 1px solid #ff3333; margin: 15px 0;'>
        <p style='color: #00d9ff; font-size: 0.9em; margin: 8px 0; letter-spacing: 0.5px;'>
        📍 Engineered with Cutting-Edge Technology & Innovation</p>
        <p style='color: #ff3333; font-weight: 900; font-size: 0.9em; margin: 8px 0;'>
        © 2026 NEXUS INTELLIGENCE SYSTEMS | System Status: <span style="color: #00ff88; text-shadow: 0 0 8px #00ff88;">✅ FULLY OPERATIONAL</span></p>
        <p style='color: #ffaa00; font-size: 0.85em; margin-top: 10px; letter-spacing: 0.5px;'>
        🌟 Transforming Anime Analytics into Rocket Science 🌟</p>
        <hr style='border: 1px solid #00ff88; margin: 15px 0;'>
        <p style='color: #00ff88; font-weight: 900; font-size: 0.95em; margin: 10px 0; letter-spacing: 2px;
                  text-shadow: 0 0 10px #00ff88;'>
        ⚡ POWERED BY DEV SHAIKH X ⚡</p>
    </div>
""", unsafe_allow_html=True)