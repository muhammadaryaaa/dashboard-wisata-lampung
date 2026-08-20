from pathlib import Path
from html import escape

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from streamlit_option_menu import option_menu


# ============================================================
# 1. PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Dashboard Wisata Lampung",
    page_icon="🏝️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# 2. MODERN LIGHT THEME CSS
# ============================================================
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

        :root {
            --primary: #4F46E5;
            --primary-soft: #EEF2FF;
            --secondary: #06B6D4;
            --accent: #10B981;
            --warning: #F59E0B;
            --danger: #EF4444;
            --text-main: #0F172A;
            --text-muted: #64748B;
            --border: #E2E8F0;
            --card: rgba(255, 255, 255, 0.86);
            --bg: #F8FAFC;
        }

        html, body, [class*="css"], .stApp {
            font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(99, 102, 241, 0.12), transparent 34rem),
                radial-gradient(circle at top right, rgba(14, 165, 233, 0.11), transparent 32rem),
                linear-gradient(180deg, #F8FAFC 0%, #F1F5F9 100%);
            color: var(--text-main);
        }

        #MainMenu, footer, header {visibility: hidden;}

        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 2.2rem;
            max-width: 1500px;
        }

        [data-testid="stSidebar"] {
            background:
                linear-gradient(180deg, rgba(255,255,255,0.96) 0%, rgba(238,242,255,0.92) 100%);
            border-right: 1px solid rgba(226, 232, 240, 0.9);
            box-shadow: 10px 0 30px rgba(15, 23, 42, 0.04);
        }

        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] span {
            color: #334155;
        }

        .brand-card {
            background: linear-gradient(135deg, #FFFFFF 0%, #EEF2FF 100%);
            border: 1px solid #DDE4FF;
            border-radius: 24px;
            padding: 20px 18px;
            margin: 4px 8px 18px 8px;
            text-align: center;
            box-shadow: 0 14px 38px rgba(79, 70, 229, 0.11);
        }

        .brand-icon {
            width: 58px;
            height: 58px;
            margin: 0 auto 10px auto;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 18px;
            background: linear-gradient(135deg, #4F46E5, #06B6D4);
            color: white;
            font-size: 1.75rem;
            box-shadow: 0 12px 24px rgba(79, 70, 229, 0.28);
        }

        .brand-card h2 {
            margin: 0;
            font-size: 1.18rem;
            line-height: 1.25;
            font-weight: 900;
            letter-spacing: -0.02em;
            color: #1E1B4B;
        }

        .brand-card p {
            margin: 6px 0 0 0;
            font-size: 0.8rem;
            color: #64748B;
        }

        .page-header {
            position: relative;
            overflow: hidden;
            border-radius: 28px;
            padding: 30px 34px;
            margin-bottom: 26px;
            background:
                linear-gradient(135deg, rgba(79,70,229,0.95) 0%, rgba(37,99,235,0.92) 42%, rgba(6,182,212,0.88) 100%);
            color: #FFFFFF;
            border: 1px solid rgba(255, 255, 255, 0.26);
            box-shadow: 0 22px 52px rgba(37, 99, 235, 0.22);
        }

        .page-header::before {
            content: "";
            position: absolute;
            width: 280px;
            height: 280px;
            right: -90px;
            top: -110px;
            background: rgba(255, 255, 255, 0.16);
            border-radius: 999px;
        }

        .page-header::after {
            content: "";
            position: absolute;
            width: 160px;
            height: 160px;
            right: 170px;
            bottom: -90px;
            background: rgba(255, 255, 255, 0.12);
            border-radius: 999px;
        }

        .page-header h1 {
            position: relative;
            z-index: 1;
            margin: 0;
            font-size: clamp(1.55rem, 2vw, 2.15rem);
            font-weight: 900;
            letter-spacing: -0.04em;
            color: #FFFFFF;
        }

        .page-header p {
            position: relative;
            z-index: 1;
            margin: 8px 0 0 0;
            max-width: 820px;
            font-size: 0.98rem;
            line-height: 1.65;
            color: rgba(255,255,255,0.88);
        }

        h1, h2, h3, h4 {
            color: #0F172A;
            letter-spacing: -0.02em;
        }

        div[data-testid="metric-container"] {
            min-height: 118px;
            padding: 21px 20px;
            border-radius: 22px;
            background: rgba(255, 255, 255, 0.88);
            border: 1px solid rgba(226, 232, 240, 0.92);
            box-shadow: 0 14px 34px rgba(15, 23, 42, 0.075);
            backdrop-filter: blur(18px);
            transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
        }

        div[data-testid="metric-container"]:hover {
            transform: translateY(-3px);
            border-color: rgba(99, 102, 241, 0.35);
            box-shadow: 0 20px 48px rgba(79, 70, 229, 0.13);
        }

        div[data-testid="metric-container"] label {
            font-size: 0.78rem;
            font-weight: 800;
            color: #64748B;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
            font-size: clamp(1.35rem, 1.65vw, 1.95rem);
            font-weight: 900;
            letter-spacing: -0.045em;
            color: #312E81;
        }

        div[data-testid="stTabs"] [data-baseweb="tab-list"] {
            gap: 10px;
            padding: 6px;
            border-radius: 18px;
            background: rgba(226, 232, 240, 0.65);
            border: 1px solid rgba(226, 232, 240, 0.9);
            width: fit-content;
        }

        div[data-testid="stTabs"] [data-baseweb="tab"] {
            height: 44px;
            border-radius: 13px;
            padding: 10px 18px;
            font-weight: 800;
            color: #64748B;
        }

        div[data-testid="stTabs"] [aria-selected="true"] {
            background: #FFFFFF !important;
            color: #4F46E5 !important;
            box-shadow: 0 8px 20px rgba(15, 23, 42, 0.08);
        }

        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        div[data-baseweb="base-input"],
        textarea {
            border-radius: 14px !important;
            border-color: #CBD5E1 !important;
            background-color: rgba(255, 255, 255, 0.92) !important;
        }

        .stDataFrame {
            border-radius: 18px;
            overflow: hidden;
            border: 1px solid rgba(226, 232, 240, 0.9);
            box-shadow: 0 16px 36px rgba(15, 23, 42, 0.07);
        }

        .stDownloadButton button,
        .stButton button {
            border-radius: 14px !important;
            font-weight: 800 !important;
            border: 1px solid #C7D2FE !important;
            background: linear-gradient(135deg, #4F46E5, #06B6D4) !important;
            color: white !important;
            box-shadow: 0 12px 22px rgba(79, 70, 229, 0.20);
        }

        .chart-title {
            display: flex;
            align-items: center;
            gap: 10px;
            margin: 4px 0 12px 0;
            font-size: 1.02rem;
            font-weight: 900;
            color: #0F172A;
            letter-spacing: -0.02em;
        }

        .chart-title span {
            width: 34px;
            height: 34px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: 12px;
            background: #EEF2FF;
            color: #4F46E5;
        }

        .soft-caption {
            margin-top: -4px;
            margin-bottom: 16px;
            color: #64748B;
            font-size: 0.88rem;
        }

        .destination-card {
            border-radius: 24px;
            padding: 22px 24px;
            background: rgba(255,255,255,0.9);
            border: 1px solid rgba(226,232,240,0.95);
            box-shadow: 0 16px 38px rgba(15,23,42,0.07);
            margin-bottom: 16px;
        }

        .destination-card h3 {
            margin: 0 0 8px 0;
            color: #1E1B4B;
            font-size: 1.25rem;
            font-weight: 900;
        }

        .pill-row {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin: 10px 0 14px 0;
        }

        .pill {
            display: inline-flex;
            align-items: center;
            padding: 7px 11px;
            border-radius: 999px;
            background: #EEF2FF;
            color: #3730A3;
            font-weight: 800;
            font-size: 0.78rem;
            border: 1px solid #C7D2FE;
        }

        .detail-box {
            padding: 16px 18px;
            border-radius: 18px;
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            color: #334155;
            line-height: 1.65;
            font-size: 0.94rem;
        }

        hr {
            border: 0;
            border-top: 1px solid rgba(226, 232, 240, 0.9);
            margin: 1.35rem 0;
        }



        .info-card, .feature-card, .insight-card, .footer-card, .hint-card, .recommend-card {
            position: relative;
            overflow: hidden;
            border-radius: 22px;
            background: rgba(255,255,255,0.9);
            border: 1px solid rgba(226,232,240,0.95);
            box-shadow: 0 16px 38px rgba(15,23,42,0.07);
        }

        .info-card {
            padding: 22px 24px;
            min-height: 142px;
        }

        .feature-card {
            padding: 20px 22px;
            min-height: 150px;
            transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
        }

        .feature-card:hover {
            transform: translateY(-3px);
            border-color: rgba(6,182,212,0.32);
            box-shadow: 0 20px 48px rgba(6,182,212,0.12);
        }

        .feature-icon {
            width: 42px;
            height: 42px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: 15px;
            background: linear-gradient(135deg, #EEF2FF, #E0F2FE);
            color: #3730A3;
            font-size: 1.24rem;
            margin-bottom: 12px;
            border: 1px solid #C7D2FE;
        }

        .feature-card h3, .info-card h3, .recommend-card h3 {
            margin: 0 0 8px 0;
            color: #1E1B4B;
            font-size: 1.03rem;
            font-weight: 900;
        }

        .feature-card p, .info-card p, .recommend-card p {
            margin: 0;
            color: #64748B;
            line-height: 1.65;
            font-size: 0.9rem;
        }

        .insight-card {
            padding: 18px 20px;
            border-left: 5px solid #4F46E5;
            background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFC 100%);
            margin-bottom: 12px;
        }

        .insight-card b {
            color: #312E81;
        }

        .hint-card {
            padding: 14px 16px;
            margin: 0 0 18px 0;
            background: linear-gradient(135deg, #F0F9FF 0%, #EEF2FF 100%);
            border-color: #BFDBFE;
            color: #334155;
            font-size: 0.88rem;
            line-height: 1.6;
        }

        .recommend-card {
            padding: 20px 22px;
            margin-bottom: 16px;
            border-left: 5px solid #10B981;
        }

        .rank-badge {
            width: 38px;
            height: 38px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: 14px;
            background: linear-gradient(135deg, #4F46E5, #06B6D4);
            color: #FFFFFF;
            font-weight: 900;
            margin-right: 10px;
        }

        .footer-card {
            margin-top: 28px;
            padding: 18px 22px;
            text-align: center;
            color: #64748B;
            font-size: 0.86rem;
            background: rgba(255,255,255,0.74);
        }

        .footer-card b {
            color: #312E81;
        }

        .dataset-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            overflow: hidden;
            border-radius: 18px;
            border: 1px solid #E2E8F0;
            background: #FFFFFF;
            box-shadow: 0 16px 36px rgba(15,23,42,0.06);
        }

        .dataset-table th {
            background: #EEF2FF;
            color: #312E81;
            padding: 13px 14px;
            text-align: left;
            font-size: 0.84rem;
        }

        .dataset-table td {
            padding: 13px 14px;
            border-top: 1px solid #E2E8F0;
            color: #334155;
            font-size: 0.86rem;
            vertical-align: top;
        }

        @media (max-width: 900px) {
            .block-container {padding-left: 1rem; padding-right: 1rem;}
            .page-header {padding: 24px 22px; border-radius: 22px;}
            div[data-testid="stTabs"] [data-baseweb="tab-list"] {width: 100%; overflow-x: auto;}
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# 3. DATA LOADING
# ============================================================
@st.cache_data
def load_data():
    data_path = Path(__file__).parent / "Dataset_Destinasi_Wisata_Provinsi_Lampung.csv"
    df = pd.read_csv(data_path)
    df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce").fillna(0)
    df["Jumlah Review"] = pd.to_numeric(df["Jumlah Review"], errors="coerce").fillna(0).astype(int)
    df["Harga Tiket"] = pd.to_numeric(df["Harga Tiket"], errors="coerce").fillna(0).astype(int)
    df["Pengikut IG"] = pd.to_numeric(df["Pengikut IG"], errors="coerce").fillna(0).astype(int)
    if "Kategori" in df.columns:
        df["Kategori"] = df["Kategori"].str.strip()
    if "Lokasi" in df.columns:
        df["Lokasi"] = df["Lokasi"].str.strip()
    df["Segment Harga"] = pd.cut(
        df["Harga Tiket"],
        bins=[-1, 0, 10000, 50000, float("inf")],
        labels=["Gratis", "Murah", "Sedang", "Mahal"],
    ).astype(str)
    return df


try:
    df = load_data()
except FileNotFoundError:
    st.error(
        "⚠️ File Dataset_Destinasi_Wisata_Provinsi_Lampung.csv tidak ditemukan. "
        "Pastikan file dataset berada di folder yang sama dengan app.py."
    )
    st.stop()


# ============================================================
# 4. HELPERS AND CHART STYLE
# ============================================================
def fmt_num(n):
    return f"{int(n):,}".replace(",", ".")


def chart_title(icon, title, caption=None):
    st.markdown(
        f"""
        <div class="chart-title"><span>{icon}</span>{title}</div>
        {f'<div class="soft-caption">{caption}</div>' if caption else ''}
        """,
        unsafe_allow_html=True,
    )


def show_chart(fig):
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False, "responsive": True})


PLOTLY_LAYOUT = dict(
    template="plotly_white",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", color="#334155", size=13),
    margin=dict(l=20, r=20, t=45, b=30),
    hoverlabel=dict(
        bgcolor="#FFFFFF",
        font_size=13,
        font_family="Inter, sans-serif",
        bordercolor="#E2E8F0",
    ),
    xaxis=dict(
        gridcolor="rgba(226,232,240,0.75)",
        zerolinecolor="rgba(203,213,225,0.9)",
        linecolor="rgba(203,213,225,0.85)",
    ),
    yaxis=dict(
        gridcolor="rgba(226,232,240,0.75)",
        zerolinecolor="rgba(203,213,225,0.9)",
        linecolor="rgba(203,213,225,0.85)",
    ),
)

CATEGORY_COLORS = {
    "Alam": "#10B981",
    "Buatan": "#4F46E5",
    "Budaya": "#F59E0B",
    "Kuliner": "#EF4444",
    "Cafe": "#EC4899",
    "Hotel": "#06B6D4",
}
GRADIENT_INDIGO = ["#EEF2FF", "#C7D2FE", "#A5B4FC", "#818CF8", "#6366F1", "#4F46E5", "#4338CA"]
GRADIENT_EMERALD = ["#ECFDF5", "#A7F3D0", "#6EE7B7", "#34D399", "#10B981", "#059669", "#047857"]
GRADIENT_AMBER = ["#FFFBEB", "#FDE68A", "#FCD34D", "#FBBF24", "#F59E0B", "#D97706", "#B45309"]
PASTEL_SET = ["#818CF8", "#34D399", "#FBBF24", "#F87171", "#F472B6", "#22D3EE", "#A78BFA", "#FB923C"]



def render_hint(extra=""):
    note = (
        "Arahkan kursor pada grafik untuk melihat detail. Klik legenda untuk menyembunyikan atau menampilkan kategori. "
        "Jika tampilan grafik berubah setelah zoom atau klik, klik dua kali pada area visualisasi untuk kembali ke tampilan awal."
    )
    if extra:
        note += " " + extra
    st.markdown(f"<div class='hint-card'>💡 {escape(note)}</div>", unsafe_allow_html=True)


def render_footer():
    st.markdown(
        """
        <div class="footer-card">
            <b>Dashboard Wisata Lampung</b><br>
            Project analisis destinasi wisata Provinsi Lampung berbasis Streamlit, Python, Pandas, dan Plotly. Tahun 2026.
        </div>
        """,
        unsafe_allow_html=True,
    )


def get_first_value(series, default="Tidak tersedia"):
    clean = series.dropna()
    if clean.empty:
        return default
    return clean.iloc[0]


def filtered_csv(dataframe):
    return dataframe.to_csv(index=False).encode("utf-8")


def build_recommendation_score(dataframe):
    rec = dataframe.copy()
    if rec.empty:
        return rec
    max_review = rec["Jumlah Review"].max() or 1
    max_ig = rec["Pengikut IG"].max() or 1
    max_price = rec["Harga Tiket"].max() or 1
    rec["Skor Rekomendasi"] = (
        rec["Rating"].fillna(0) * 40
        + (np.log1p(rec["Jumlah Review"]) / np.log1p(max_review)) * 30
        + (np.log1p(rec["Pengikut IG"]) / np.log1p(max_ig)) * 20
        + (1 - (rec["Harga Tiket"].fillna(0) / max_price).clip(0, 1)) * 10
    ).round(2)
    return rec.sort_values("Skor Rekomendasi", ascending=False)


def render_insight_cards(dataframe):
    if dataframe.empty:
        return
    top_rating = dataframe.sort_values(["Rating", "Jumlah Review"], ascending=[False, False]).iloc[0]
    top_review = dataframe.sort_values("Jumlah Review", ascending=False).iloc[0]
    top_lokasi = dataframe["Lokasi"].value_counts().idxmax()
    top_kategori = dataframe["Kategori"].value_counts().idxmax()
    gratis_count = int((dataframe["Harga Tiket"] == 0).sum())
    st.markdown(
        f"""
        <div class="insight-card">⭐ Destinasi dengan rating tertinggi pada filter saat ini adalah <b>{escape(str(top_rating['Nama Tempat']))}</b> dengan rating <b>{float(top_rating['Rating']):.1f}</b>.</div>
        <div class="insight-card">📝 Destinasi dengan review terbanyak adalah <b>{escape(str(top_review['Nama Tempat']))}</b> dengan total <b>{fmt_num(top_review['Jumlah Review'])}</b> review.</div>
        <div class="insight-card">📍 Lokasi dengan jumlah destinasi terbanyak adalah <b>{escape(str(top_lokasi))}</b>, sedangkan kategori paling dominan adalah <b>{escape(str(top_kategori))}</b>.</div>
        <div class="insight-card">💰 Terdapat <b>{fmt_num(gratis_count)}</b> destinasi dengan harga tiket gratis pada data yang sedang ditampilkan.</div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# 5. SIDEBAR NAVIGATION AND FILTERS
# ============================================================
with st.sidebar:
    st.markdown(
        """
        <div class="brand-card">
            <div class="brand-icon">🏝️</div>
            <h2>Wisata Lampung</h2>
            <p>Dashboard Analytics</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    selected_menu = option_menu(
        menu_title=None,
        options=[
            "Beranda",
            "Overview",
            "Kategori & Harga",
            "Eksplorasi Lokasi",
            "Popularitas & Sosmed",
            "Rekomendasi Destinasi",
            "Eksplorasi Data",
            "Tentang Dataset",
            "Data Detail",
        ],
        icons=[
            "house-heart-fill",
            "grid-1x2-fill",
            "pie-chart-fill",
            "geo-alt-fill",
            "graph-up-arrow",
            "stars",
            "search",
            "database-fill",
            "table",
        ],
        default_index=0,
        styles={
            "container": {"padding": "4px 6px", "background-color": "transparent"},
            "icon": {"color": "#4F46E5", "font-size": "17px"},
            "nav-link": {
                "font-size": "14px",
                "text-align": "left",
                "margin": "6px 4px",
                "padding": "12px 14px",
                "--hover-color": "#E0F2FE",
                "border-radius": "14px",
                "color": "#334155",
                "font-weight": "700",
            },
            "nav-link-selected": {
                "background": "linear-gradient(135deg, #4F46E5, #06B6D4)",
                "color": "white",
                "font-weight": "800",
                "border-radius": "14px",
                "box-shadow": "0 12px 22px rgba(79,70,229,0.24)",
            },
        },
    )

    st.markdown("---")
    st.markdown("##### 🔍 Filter Global")
    st.caption("Filter berlaku di semua halaman")

    lokasi_list = sorted(df["Lokasi"].dropna().unique().tolist())
    selected_lokasi = st.selectbox("📍 Lokasi", ["Semua"] + lokasi_list)

    kategori_list = sorted(df["Kategori"].dropna().unique().tolist())
    selected_kategori = st.selectbox("🏷️ Kategori", ["Semua"] + kategori_list)

    min_rating, max_rating = st.slider(
        "⭐ Rentang Rating",
        min_value=0.0,
        max_value=5.0,
        value=(0.0, 5.0),
        step=0.1,
    )

    selected_harga = st.selectbox(
        "💰 Segment Harga",
        ["Semua", "Gratis", "Murah", "Sedang", "Mahal"],
        help="Gratis = Rp 0, Murah = sampai Rp 10.000, Sedang = Rp 10.001 sampai Rp 50.000, Mahal = di atas Rp 50.000",
    )

    st.markdown("---")
    st.markdown(
        "<p style='text-align:center; color:#94A3B8; font-size:0.74rem;'>© 2026 Wisata Lampung Dashboard</p>",
        unsafe_allow_html=True,
    )


# ============================================================
# 6. APPLY FILTERS
# ============================================================
df_filtered = df.copy()
if selected_lokasi != "Semua":
    df_filtered = df_filtered[df_filtered["Lokasi"] == selected_lokasi]
if selected_kategori != "Semua":
    df_filtered = df_filtered[df_filtered["Kategori"] == selected_kategori]
df_filtered = df_filtered[(df_filtered["Rating"] >= min_rating) & (df_filtered["Rating"] <= max_rating)]
if selected_harga != "Semua":
    df_filtered = df_filtered[df_filtered["Segment Harga"] == selected_harga]

with st.sidebar:
    st.download_button(
        "📥 Download Data Filter",
        filtered_csv(df_filtered),
        "wisata_lampung_data_filter.csv",
        "text/csv",
        use_container_width=True,
    )

if df_filtered.empty:
    st.warning("⚠️ Tidak ada data yang cocok dengan filter. Ubah opsi filter di sidebar.")
    st.stop()


# ============================================================
# PAGE: BERANDA
# ============================================================
if selected_menu == "Beranda":
    st.markdown(
        """
        <div class="page-header">
            <h1>🏝️ Dashboard Analisis Destinasi Wisata Lampung</h1>
            <p>Dashboard ini menyajikan ringkasan, eksplorasi lokasi, analisis kategori, rekomendasi destinasi, pencarian data, dan informasi dataset secara interaktif.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    b1, b2, b3, b4 = st.columns(4)
    with b1:
        st.metric("Total Destinasi", fmt_num(len(df_filtered)))
    with b2:
        st.metric("Jumlah Lokasi", fmt_num(df_filtered["Lokasi"].nunique()))
    with b3:
        st.metric("Jumlah Kategori", fmt_num(df_filtered["Kategori"].nunique()))
    with b4:
        st.metric("Rating Rata rata", f"⭐ {df_filtered['Rating'].mean():.2f}")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### ✨ Fitur Utama Dashboard")
    f1, f2, f3, f4 = st.columns(4)
    with f1:
        st.markdown("""
        <div class="feature-card"><div class="feature-icon">📊</div><h3>Overview</h3><p>Melihat ringkasan jumlah destinasi, rating, review, harga tiket, serta grafik utama.</p></div>
        """, unsafe_allow_html=True)
    with f2:
        st.markdown("""
        <div class="feature-card"><div class="feature-icon">🗺️</div><h3>Eksplorasi Lokasi</h3><p>Menganalisis persebaran destinasi berdasarkan kabupaten dan kota di Lampung.</p></div>
        """, unsafe_allow_html=True)
    with f3:
        st.markdown("""
        <div class="feature-card"><div class="feature-icon">⭐</div><h3>Rekomendasi</h3><p>Menampilkan destinasi terbaik berdasarkan rating, review, followers Instagram, dan harga.</p></div>
        """, unsafe_allow_html=True)
    with f4:
        st.markdown("""
        <div class="feature-card"><div class="feature-icon">🔎</div><h3>Eksplorasi Data</h3><p>Mencari destinasi wisata dan melihat detail fasilitas, harga tiket, review, serta lokasi.</p></div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 💡 Insight Otomatis")
    render_insight_cards(df_filtered)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns([1.1, 1])
    with c1:
        chart_title("🏷️", "Distribusi Kategori Utama")
        kategori_home = df_filtered["Kategori"].value_counts().reset_index()
        kategori_home.columns = ["Kategori", "Jumlah"]
        fig_home = px.bar(
            kategori_home,
            x="Kategori",
            y="Jumlah",
            color="Kategori",
            color_discrete_map=CATEGORY_COLORS,
            text="Jumlah",
        )
        fig_home.update_traces(textposition="outside", marker_line_width=0)
        fig_home.update_layout(**PLOTLY_LAYOUT, height=360, showlegend=False, xaxis_title="Kategori", yaxis_title="Jumlah")
        show_chart(fig_home)
    with c2:
        chart_title("📍", "Top 7 Lokasi dengan Destinasi Terbanyak")
        lokasi_home = df_filtered["Lokasi"].value_counts().head(7).sort_values(ascending=True).reset_index()
        lokasi_home.columns = ["Lokasi", "Jumlah"]
        fig_home2 = px.bar(
            lokasi_home,
            x="Jumlah",
            y="Lokasi",
            orientation="h",
            color="Jumlah",
            color_continuous_scale=GRADIENT_INDIGO,
            text="Jumlah",
        )
        fig_home2.update_traces(textposition="outside", marker_line_width=0)
        fig_home2.update_layout(**PLOTLY_LAYOUT, height=360, showlegend=False, coloraxis_showscale=False, xaxis_title="Jumlah", yaxis_title="")
        show_chart(fig_home2)

    st.markdown("<br>", unsafe_allow_html=True)
    st.download_button(
        "📥 Download Data Sesuai Filter",
        filtered_csv(df_filtered),
        "wisata_lampung_data_beranda.csv",
        "text/csv",
        use_container_width=True,
    )


# ============================================================
# PAGE: OVERVIEW
# ============================================================
elif selected_menu == "Overview":
    st.markdown(
        """
        <div class="page-header">
            <h1>🌟 Overview Destinasi Wisata</h1>
            <p>Ringkasan performa, rating, review, harga tiket, dan popularitas destinasi wisata di Provinsi Lampung.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_hint()

    k1, k2, k3, k4, k5 = st.columns(5)
    with k1:
        st.metric("Total Destinasi", fmt_num(len(df_filtered)))
    with k2:
        avg_r = round(df_filtered["Rating"].mean(), 2) if not df_filtered.empty else 0
        st.metric("Rata rata Rating", f"⭐ {avg_r}")
    with k3:
        st.metric("Total Review", fmt_num(df_filtered["Jumlah Review"].sum()))
    with k4:
        avg_harga = int(df_filtered["Harga Tiket"].mean())
        st.metric("Rata rata Harga", f"Rp {fmt_num(avg_harga)}")
    with k5:
        total_ig = df_filtered["Pengikut IG"].sum()
        st.metric("Total Followers IG", fmt_num(total_ig))

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        chart_title("🏆", "Top 10 Terpopuler Berdasarkan Review")
        top10_rev = df_filtered.nlargest(10, "Jumlah Review").sort_values("Jumlah Review", ascending=True)
        fig = px.bar(
            top10_rev,
            x="Jumlah Review",
            y="Nama Tempat",
            orientation="h",
            color="Jumlah Review",
            color_continuous_scale=GRADIENT_INDIGO,
            text="Jumlah Review",
        )
        fig.update_traces(texttemplate="%{text:,}", textposition="outside", textfont_size=11, marker_line_width=0)
        fig.update_layout(
            **PLOTLY_LAYOUT,
            showlegend=False,
            coloraxis_showscale=False,
            yaxis_title="",
            xaxis_title="Jumlah Review",
            height=420,
        )
        show_chart(fig)

    with c2:
        chart_title("⭐", "Top 10 Rating Tertinggi", "Data ditampilkan dari destinasi dengan minimal 20 review.")
        df_valid = df_filtered[df_filtered["Jumlah Review"] >= 20]
        if not df_valid.empty:
            top10_rat = df_valid.nlargest(10, "Rating").sort_values("Rating", ascending=True)
            fig2 = px.bar(
                top10_rat,
                x="Rating",
                y="Nama Tempat",
                orientation="h",
                color="Rating",
                color_continuous_scale=GRADIENT_EMERALD,
                text="Rating",
            )
            fig2.update_traces(texttemplate="%{text:.1f}", textposition="outside", textfont_size=11, marker_line_width=0)
            fig2.update_layout(
                **PLOTLY_LAYOUT,
                showlegend=False,
                coloraxis_showscale=False,
                yaxis_title="",
                xaxis_title="Rating",
                height=420,
            )
            fig2.update_xaxes(range=[3.5, 5.2])
            show_chart(fig2)
        else:
            st.info("Data tidak cukup untuk menampilkan destinasi dengan minimal 20 review.")

    st.markdown("<br>", unsafe_allow_html=True)

    c3, c4 = st.columns(2)
    with c3:
        chart_title("📊", "Distribusi Rating Destinasi")
        fig3 = px.histogram(
            df_filtered,
            x="Rating",
            nbins=20,
            color_discrete_sequence=["#818CF8"],
            opacity=0.86,
        )
        fig3.update_traces(marker_line_color="#FFFFFF", marker_line_width=1)
        fig3.update_layout(
            **PLOTLY_LAYOUT,
            bargap=0.08,
            height=380,
            xaxis_title="Rating",
            yaxis_title="Jumlah Destinasi",
        )
        show_chart(fig3)

    with c4:
        chart_title("🌐", "Komposisi Kategori per Lokasi")
        sun_data = (
            df_filtered.dropna(subset=["Kategori", "Lokasi"])
            .groupby(["Kategori", "Lokasi"])
            .size()
            .reset_index(name="Jumlah")
        )
        if not sun_data.empty:
            fig4 = px.sunburst(
                sun_data,
                path=["Kategori", "Lokasi"],
                values="Jumlah",
                color="Kategori",
                color_discrete_map=CATEGORY_COLORS,
            )
            fig4.update_layout(**PLOTLY_LAYOUT, height=380)
            fig4.update_traces(textinfo="label+percent parent", insidetextorientation="radial")
            show_chart(fig4)
        else:
            st.info("Data kategori dan lokasi belum tersedia untuk ditampilkan.")


# ============================================================
# PAGE: KATEGORI & HARGA
# ============================================================
elif selected_menu == "Kategori & Harga":
    st.markdown(
        """
        <div class="page-header">
            <h1>📊 Analisis Kategori & Harga Tiket</h1>
            <p>Sebaran kategori wisata, komparasi harga tiket, serta perbandingan metrik utama pada setiap kategori.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_hint("Pada treemap, klik kotak kategori untuk memperbesar bagian tertentu dan klik dua kali untuk mengembalikan tampilan.")

    tab1, tab2, tab3 = st.tabs(["🎯 Proporsi Kategori", "💰 Analisis Harga", "📈 Perbandingan"])

    with tab1:
        c1, c2 = st.columns([1, 1.2])
        with c1:
            chart_title("🎯", "Donut Chart Kategori")
            kat_count = df_filtered["Kategori"].value_counts().reset_index()
            kat_count.columns = ["Kategori", "Jumlah"]
            fig = px.pie(
                kat_count,
                values="Jumlah",
                names="Kategori",
                color="Kategori",
                color_discrete_map=CATEGORY_COLORS,
                hole=0.55,
            )
            fig.update_traces(
                textposition="outside",
                textinfo="label+percent",
                textfont_size=12,
                pull=[0.03] * len(kat_count),
                marker=dict(line=dict(color="#FFFFFF", width=2)),
            )
            fig.update_layout(**PLOTLY_LAYOUT, height=420, showlegend=False)
            fig.add_annotation(
                text=f"<b>{len(df_filtered)}</b><br><span style='font-size:11px;color:#94A3B8'>destinasi</span>",
                showarrow=False,
                font=dict(size=22, color="#4338CA"),
            )
            show_chart(fig)

        with c2:
            chart_title("🧭", "Treemap Kategori × Lokasi")
            fig2 = px.treemap(
                df_filtered,
                path=["Kategori", "Lokasi"],
                color="Kategori",
                color_discrete_map=CATEGORY_COLORS,
            )
            fig2.update_layout(**PLOTLY_LAYOUT, height=420)
            fig2.update_traces(textinfo="label+value", textfont_size=12)
            show_chart(fig2)

    with tab2:
        c1, c2 = st.columns(2)
        with c1:
            chart_title("💰", "Box Plot Harga per Kategori")
            q99 = df_filtered["Harga Tiket"].quantile(0.95)
            df_box = df_filtered[df_filtered["Harga Tiket"] <= q99]
            fig3 = px.box(
                df_box,
                x="Kategori",
                y="Harga Tiket",
                color="Kategori",
                color_discrete_map=CATEGORY_COLORS,
                points="outliers",
            )
            fig3.update_layout(
                **PLOTLY_LAYOUT,
                height=420,
                showlegend=False,
                xaxis_title="Kategori",
                yaxis_title="Harga Tiket (Rp)",
            )
            show_chart(fig3)

        with c2:
            chart_title("✨", "Scatter Harga vs Rating")
            fig4 = px.scatter(
                df_filtered[df_filtered["Harga Tiket"] <= q99],
                x="Rating",
                y="Harga Tiket",
                size="Jumlah Review",
                color="Kategori",
                hover_name="Nama Tempat",
                color_discrete_map=CATEGORY_COLORS,
                size_max=30,
                opacity=0.78,
            )
            fig4.update_traces(marker=dict(line=dict(width=0.8, color="#FFFFFF")))
            fig4.update_layout(
                **PLOTLY_LAYOUT,
                height=420,
                xaxis_title="Rating",
                yaxis_title="Harga Tiket (Rp)",
            )
            show_chart(fig4)

    with tab3:
        chart_title("📈", "Rata rata Metrik per Kategori")
        comp = df_filtered.groupby("Kategori").agg(
            Jumlah=("Nama Tempat", "count"),
            Avg_Rating=("Rating", "mean"),
            Avg_Harga=("Harga Tiket", "mean"),
            Avg_Review=("Jumlah Review", "mean"),
            Avg_IG=("Pengikut IG", "mean"),
        ).reset_index()
        comp["Avg_Rating"] = comp["Avg_Rating"].round(2)
        comp["Avg_Harga"] = comp["Avg_Harga"].astype(int)
        comp["Avg_Review"] = comp["Avg_Review"].astype(int)
        comp["Avg_IG"] = comp["Avg_IG"].astype(int)

        fig5 = go.Figure()
        fig5.add_trace(
            go.Bar(
                name="Avg Rating ×1000",
                x=comp["Kategori"],
                y=comp["Avg_Rating"] * 1000,
                marker_color="#818CF8",
                text=comp["Avg_Rating"].apply(lambda x: f"{x:.2f}"),
                textposition="outside",
            )
        )
        fig5.add_trace(
            go.Bar(
                name="Avg Harga (Rp)",
                x=comp["Kategori"],
                y=comp["Avg_Harga"],
                marker_color="#34D399",
                text=comp["Avg_Harga"].apply(lambda x: f"Rp {x:,}".replace(",", ".")),
                textposition="outside",
            )
        )
        fig5.add_trace(
            go.Bar(
                name="Avg Review",
                x=comp["Kategori"],
                y=comp["Avg_Review"],
                marker_color="#FBBF24",
                text=comp["Avg_Review"].apply(lambda x: f"{x:,}".replace(",", ".")),
                textposition="outside",
            )
        )
        fig5.update_layout(
            **PLOTLY_LAYOUT,
            barmode="group",
            height=440,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
            xaxis_title="Kategori",
            yaxis_title="Nilai",
        )
        show_chart(fig5)


# ============================================================
# PAGE: EKSPLORASI LOKASI
# ============================================================
elif selected_menu == "Eksplorasi Lokasi":
    st.markdown(
        """
        <div class="page-header">
            <h1>🗺️ Eksplorasi Berdasarkan Lokasi</h1>
            <p>Distribusi destinasi wisata di setiap kabupaten dan kota di Provinsi Lampung.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_hint("Pada grafik lokasi yang panjang, gunakan scroll halaman untuk melihat semua daerah.")

    tab1, tab2, tab3 = st.tabs(["📊 Distribusi Lokasi", "🔥 Heatmap", "📍 Detail Lokasi"])

    with tab1:
        chart_title("📊", "Jumlah Destinasi per Daerah")
        lok_count = df_filtered["Lokasi"].value_counts().reset_index()
        lok_count.columns = ["Lokasi", "Jumlah"]
        lok_count = lok_count.sort_values("Jumlah", ascending=True)

        fig = px.bar(
            lok_count,
            x="Jumlah",
            y="Lokasi",
            orientation="h",
            color="Jumlah",
            color_continuous_scale=GRADIENT_INDIGO,
            text="Jumlah",
        )
        fig.update_traces(textposition="outside", textfont_size=12, marker_line_width=0)
        fig.update_layout(
            **PLOTLY_LAYOUT,
            height=max(400, len(lok_count) * 35),
            showlegend=False,
            coloraxis_showscale=False,
            yaxis_title="",
            xaxis_title="Jumlah Destinasi",
        )
        show_chart(fig)

    with tab2:
        chart_title("🔥", "Heatmap Lokasi × Kategori")
        heat = df_filtered.groupby(["Lokasi", "Kategori"]).size().reset_index(name="Jumlah")
        heat_pivot = heat.pivot_table(index="Lokasi", columns="Kategori", values="Jumlah", fill_value=0)

        fig2 = go.Figure(
            data=go.Heatmap(
                z=heat_pivot.values,
                x=heat_pivot.columns.tolist(),
                y=heat_pivot.index.tolist(),
                colorscale="Purples",
                text=heat_pivot.values,
                texttemplate="%{text}",
                hovertemplate="Lokasi: %{y}<br>Kategori: %{x}<br>Jumlah: %{z}<extra></extra>",
                colorbar=dict(title="Jumlah"),
            )
        )
        fig2.update_layout(
            **PLOTLY_LAYOUT,
            height=max(400, len(heat_pivot) * 32),
            xaxis_title="Kategori",
            yaxis_title="Lokasi",
        )
        show_chart(fig2)

    with tab3:
        chart_title("📍", "Rata rata Rating & Harga per Lokasi")
        lok_stats = df_filtered.groupby("Lokasi").agg(
            Jumlah=("Nama Tempat", "count"),
            Avg_Rating=("Rating", "mean"),
            Avg_Harga=("Harga Tiket", "mean"),
            Total_Review=("Jumlah Review", "sum"),
        ).reset_index().sort_values("Avg_Rating", ascending=False)
        lok_stats["Avg_Rating"] = lok_stats["Avg_Rating"].round(2)
        lok_stats["Avg_Harga"] = lok_stats["Avg_Harga"].astype(int)

        fig3 = go.Figure()
        fig3.add_trace(
            go.Bar(
                name="Avg Rating",
                x=lok_stats["Lokasi"],
                y=lok_stats["Avg_Rating"],
                marker_color="#818CF8",
                yaxis="y",
                text=lok_stats["Avg_Rating"].apply(lambda x: f"{x:.2f}"),
                textposition="outside",
                textfont_size=10,
            )
        )
        fig3.add_trace(
            go.Scatter(
                name="Avg Harga (Rp)",
                x=lok_stats["Lokasi"],
                y=lok_stats["Avg_Harga"],
                mode="lines+markers",
                line=dict(color="#F59E0B", width=3),
                marker=dict(size=8, color="#F59E0B"),
                yaxis="y2",
            )
        )
        fig3.update_layout(
            **PLOTLY_LAYOUT,
            height=460,
            yaxis2=dict(title="Avg Harga (Rp)", overlaying="y", side="right", showgrid=False),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
            xaxis_tickangle=-45,
        )
        fig3.update_yaxes(title="Avg Rating", range=[0, 5.5], gridcolor="rgba(226,232,240,0.75)")
        show_chart(fig3)


# ============================================================
# PAGE: POPULARITAS & SOSMED
# ============================================================
elif selected_menu == "Popularitas & Sosmed":
    st.markdown(
        """
        <div class="page-header">
            <h1>📱 Popularitas & Media Sosial</h1>
            <p>Analisis hubungan antara followers Instagram, jumlah review, rating, dan skor popularitas daerah.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_hint("Pada scatter plot, tarik area grafik untuk zoom dan klik dua kali untuk kembali ke tampilan awal.")

    tab1, tab2, tab3 = st.tabs(["📊 Top Followers IG", "🔗 Korelasi", "🏅 Ranking Daerah"])

    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            chart_title("🔝", "Top 15 Followers Instagram")
            top15_ig = df_filtered.nlargest(15, "Pengikut IG").sort_values("Pengikut IG", ascending=True)
            fig = px.bar(
                top15_ig,
                x="Pengikut IG",
                y="Nama Tempat",
                orientation="h",
                color="Pengikut IG",
                color_continuous_scale=["#FECDD3", "#FB7185", "#E11D48"],
                text="Pengikut IG",
            )
            fig.update_traces(texttemplate="%{text:,}", textposition="outside", textfont_size=10, marker_line_width=0)
            fig.update_layout(
                **PLOTLY_LAYOUT,
                height=520,
                showlegend=False,
                coloraxis_showscale=False,
                yaxis_title="",
                xaxis_title="Pengikut IG",
            )
            show_chart(fig)

        with c2:
            chart_title("🔝", "Top 15 Jumlah Review")
            top15_rev = df_filtered.nlargest(15, "Jumlah Review").sort_values("Jumlah Review", ascending=True)
            fig2 = px.bar(
                top15_rev,
                x="Jumlah Review",
                y="Nama Tempat",
                orientation="h",
                color="Jumlah Review",
                color_continuous_scale=GRADIENT_EMERALD,
                text="Jumlah Review",
            )
            fig2.update_traces(texttemplate="%{text:,}", textposition="outside", textfont_size=10, marker_line_width=0)
            fig2.update_layout(
                **PLOTLY_LAYOUT,
                height=520,
                showlegend=False,
                coloraxis_showscale=False,
                yaxis_title="",
                xaxis_title="Jumlah Review",
            )
            show_chart(fig2)

    with tab2:
        chart_title("🔗", "Korelasi Followers IG vs Jumlah Review")
        df_corr = df_filtered[(df_filtered["Pengikut IG"] > 0) & (df_filtered["Jumlah Review"] > 0)].copy()

        if not df_corr.empty:
            fig3 = px.scatter(
                df_corr,
                x="Pengikut IG",
                y="Jumlah Review",
                color="Kategori",
                hover_name="Nama Tempat",
                size="Rating",
                size_max=22,
                opacity=0.76,
                color_discrete_map=CATEGORY_COLORS,
                log_x=True,
                log_y=True,
            )
            fig3.update_traces(marker=dict(line=dict(width=0.8, color="#FFFFFF")))
            fig3.update_layout(
                **PLOTLY_LAYOUT,
                height=480,
                xaxis_title="Pengikut IG (log scale)",
                yaxis_title="Jumlah Review (log scale)",
            )
            show_chart(fig3)

            corr_val = df_corr["Pengikut IG"].corr(df_corr["Jumlah Review"])
            st.info(f"📈 Koefisien korelasi Pearson antara Pengikut IG dan Jumlah Review: **{corr_val:.3f}**")
        else:
            st.info("Data tidak cukup untuk analisis korelasi.")

    with tab3:
        chart_title("🏅", "Ranking Daerah Berdasarkan Skor Popularitas")
        st.caption("Skor = (Avg Rating × 20) + log(Total Review + 1) × 5 + log(Total IG + 1) × 3")

        lok_rank = df_filtered.groupby("Lokasi").agg(
            Jumlah=("Nama Tempat", "count"),
            Avg_Rating=("Rating", "mean"),
            Total_Review=("Jumlah Review", "sum"),
            Total_IG=("Pengikut IG", "sum"),
        ).reset_index()
        lok_rank["Skor"] = (
            lok_rank["Avg_Rating"] * 20
            + np.log1p(lok_rank["Total_Review"]) * 5
            + np.log1p(lok_rank["Total_IG"]) * 3
        ).round(1)
        lok_rank = lok_rank.sort_values("Skor", ascending=True)

        fig4 = px.bar(
            lok_rank,
            x="Skor",
            y="Lokasi",
            orientation="h",
            color="Skor",
            color_continuous_scale=GRADIENT_AMBER,
            text="Skor",
        )
        fig4.update_traces(textposition="outside", textfont_size=11, marker_line_width=0)
        fig4.update_layout(
            **PLOTLY_LAYOUT,
            height=max(400, len(lok_rank) * 32),
            showlegend=False,
            coloraxis_showscale=False,
            yaxis_title="",
            xaxis_title="Skor Popularitas",
        )
        show_chart(fig4)


# ============================================================
# PAGE: REKOMENDASI DESTINASI
# ============================================================
elif selected_menu == "Rekomendasi Destinasi":
    st.markdown(
        """
        <div class="page-header">
            <h1>🌟 Rekomendasi Destinasi Wisata</h1>
            <p>Pilih preferensi wisata untuk mendapatkan daftar destinasi yang paling sesuai berdasarkan rating, review, media sosial, dan harga tiket.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_hint("Grafik rekomendasi dapat dizoom. Klik dua kali pada grafik untuk mengembalikan tampilan awal.")

    rec_left, rec_mid, rec_right = st.columns(3)
    with rec_left:
        pref_kategori = st.selectbox("🏷️ Preferensi Kategori", ["Semua"] + sorted(df_filtered["Kategori"].dropna().unique().tolist()))
    with rec_mid:
        pref_lokasi = st.selectbox("📍 Preferensi Lokasi", ["Semua"] + sorted(df_filtered["Lokasi"].dropna().unique().tolist()))
    with rec_right:
        pref_rating = st.slider("⭐ Rating Minimal", 0.0, 5.0, 4.0, 0.1)

    rec_data = df_filtered.copy()
    if pref_kategori != "Semua":
        rec_data = rec_data[rec_data["Kategori"] == pref_kategori]
    if pref_lokasi != "Semua":
        rec_data = rec_data[rec_data["Lokasi"] == pref_lokasi]
    rec_data = rec_data[rec_data["Rating"] >= pref_rating]

    if rec_data.empty:
        st.warning("Belum ada destinasi yang cocok dengan preferensi tersebut. Turunkan rating minimal atau ubah filter global di sidebar.")
    else:
        rec_rank = build_recommendation_score(rec_data)
        top_rec = rec_rank.head(10)

        s1, s2, s3, s4 = st.columns(4)
        with s1:
            st.metric("Rekomendasi Tersedia", fmt_num(len(rec_rank)))
        with s2:
            st.metric("Skor Tertinggi", f"{top_rec['Skor Rekomendasi'].max():.2f}")
        with s3:
            st.metric("Rating Tertinggi", f"⭐ {top_rec['Rating'].max():.1f}")
        with s4:
            st.metric("Harga Termurah", f"Rp {fmt_num(top_rec['Harga Tiket'].min())}")

        st.markdown("<br>", unsafe_allow_html=True)
        left, right = st.columns([1.15, 1])
        with left:
            chart_title("🏆", "Top 10 Skor Rekomendasi")
            plot_rec = top_rec.sort_values("Skor Rekomendasi", ascending=True)
            fig_rec = px.bar(
                plot_rec,
                x="Skor Rekomendasi",
                y="Nama Tempat",
                orientation="h",
                color="Kategori",
                color_discrete_map=CATEGORY_COLORS,
                text="Skor Rekomendasi",
                hover_data=["Lokasi", "Rating", "Jumlah Review", "Harga Tiket", "Pengikut IG"],
            )
            fig_rec.update_traces(texttemplate="%{text:.2f}", textposition="outside", marker_line_width=0)
            fig_rec.update_layout(**PLOTLY_LAYOUT, height=460, showlegend=True, xaxis_title="Skor Rekomendasi", yaxis_title="")
            show_chart(fig_rec)

        with right:
            chart_title("✨", "Detail Rekomendasi Terbaik")
            best = top_rec.iloc[0]
            harga_best = "Gratis" if int(best["Harga Tiket"]) == 0 else f"Rp {fmt_num(best['Harga Tiket'])}"
            st.markdown(
                f"""
                <div class="recommend-card">
                    <h3><span class="rank-badge">1</span>{escape(str(best['Nama Tempat']))}</h3>
                    <div class="pill-row">
                        <span class="pill">📍 {escape(str(best['Lokasi']))}</span>
                        <span class="pill">🏷️ {escape(str(best['Kategori']))}</span>
                        <span class="pill">⭐ {float(best['Rating']):.1f}</span>
                        <span class="pill">💰 {escape(harga_best)}</span>
                    </div>
                    <p>Destinasi ini memiliki skor rekomendasi tertinggi pada filter saat ini, dengan kombinasi rating, jumlah review, pengikut Instagram, dan harga tiket yang paling seimbang.</p>
                    <div class="detail-box" style="margin-top:14px;">
                        <b>Skor Rekomendasi:</b> {float(best['Skor Rekomendasi']):.2f}<br>
                        <b>Jumlah Review:</b> {fmt_num(best['Jumlah Review'])}<br>
                        <b>Pengikut Instagram:</b> {fmt_num(best['Pengikut IG'])}<br>
                        <b>Fasilitas:</b> {escape(str(best.get('Fasilitas', '')))}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        chart_title("📋", "Daftar Rekomendasi")
        rec_cols = ["Nama Tempat", "Lokasi", "Kategori", "Rating", "Jumlah Review", "Harga Tiket", "Pengikut IG", "Skor Rekomendasi"]
        st.dataframe(
            rec_rank[rec_cols].reset_index(drop=True),
            use_container_width=True,
            hide_index=True,
            height=420,
            column_config={
                "Rating": st.column_config.NumberColumn("⭐ Rating", format="%.1f"),
                "Jumlah Review": st.column_config.NumberColumn("📝 Review", format="%d"),
                "Harga Tiket": st.column_config.NumberColumn("💰 Harga", format="Rp %d"),
                "Pengikut IG": st.column_config.NumberColumn("📱 IG Followers", format="%d"),
                "Skor Rekomendasi": st.column_config.NumberColumn("🌟 Skor", format="%.2f"),
            },
        )
        st.download_button(
            "📥 Download Data Rekomendasi",
            filtered_csv(rec_rank[rec_cols]),
            "wisata_lampung_rekomendasi.csv",
            "text/csv",
            use_container_width=True,
        )


# ============================================================
# PAGE: EKSPLORASI DATA
# ============================================================
elif selected_menu == "Eksplorasi Data":
    st.markdown(
        """
        <div class="page-header">
            <h1>🔎 Eksplorasi Data Destinasi</h1>
            <p>Cari nama destinasi wisata, lihat ringkasan data, fasilitas, ulasan, serta detail destinasi yang dipilih.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_hint("Gunakan kolom pencarian untuk menemukan nama destinasi, lokasi, kategori, fasilitas, atau isi ulasan.")

    q1, q2 = st.columns([2.2, 1])
    with q1:
        keyword = st.text_input(
            "🔎 Cari destinasi wisata",
            placeholder="Contoh: Pantai Mutun, Pahawang, Museum Lampung...",
        )
    with q2:
        sort_option = st.selectbox(
            "Urutkan hasil",
            ["Rating tertinggi", "Review terbanyak", "Followers IG terbanyak", "Harga termurah", "Nama A-Z"],
        )

    search_df = df_filtered.copy()
    if keyword:
        keyword_mask = (
            search_df["Nama Tempat"].astype(str).str.contains(keyword, case=False, na=False)
            | search_df["Lokasi"].astype(str).str.contains(keyword, case=False, na=False)
            | search_df["Kategori"].astype(str).str.contains(keyword, case=False, na=False)
            | search_df["Fasilitas"].astype(str).str.contains(keyword, case=False, na=False)
            | search_df["Review"].astype(str).str.contains(keyword, case=False, na=False)
        )
        search_df = search_df[keyword_mask]

    if sort_option == "Rating tertinggi":
        search_df = search_df.sort_values(["Rating", "Jumlah Review"], ascending=[False, False])
    elif sort_option == "Review terbanyak":
        search_df = search_df.sort_values("Jumlah Review", ascending=False)
    elif sort_option == "Followers IG terbanyak":
        search_df = search_df.sort_values("Pengikut IG", ascending=False)
    elif sort_option == "Harga termurah":
        search_df = search_df.sort_values(["Harga Tiket", "Rating"], ascending=[True, False])
    else:
        search_df = search_df.sort_values("Nama Tempat", ascending=True)

    st.markdown("<br>", unsafe_allow_html=True)
    r1, r2, r3, r4 = st.columns(4)
    with r1:
        st.metric("Hasil Ditemukan", fmt_num(len(search_df)))
    with r2:
        st.metric("Rata rata Rating", f"⭐ {search_df['Rating'].mean():.2f}" if not search_df.empty else "0")
    with r3:
        st.metric("Total Review", fmt_num(search_df["Jumlah Review"].sum()) if not search_df.empty else "0")
    with r4:
        st.metric("Lokasi Terlibat", fmt_num(search_df["Lokasi"].nunique()) if not search_df.empty else "0")

    st.markdown("<br>", unsafe_allow_html=True)

    if search_df.empty:
        st.warning("Destinasi tidak ditemukan. Coba gunakan kata kunci lain atau ubah filter global di sidebar.")
    else:
        left, right = st.columns([1.15, 1])

        with left:
            chart_title("📋", "Hasil Pencarian Destinasi")
            preview_cols = ["Nama Tempat", "Lokasi", "Kategori", "Rating", "Jumlah Review", "Harga Tiket", "Pengikut IG"]
            st.dataframe(
                search_df[preview_cols].reset_index(drop=True),
                use_container_width=True,
                hide_index=True,
                height=420,
                column_config={
                    "Rating": st.column_config.NumberColumn("⭐ Rating", format="%.1f"),
                    "Jumlah Review": st.column_config.NumberColumn("📝 Review", format="%d"),
                    "Harga Tiket": st.column_config.NumberColumn("💰 Harga", format="Rp %d"),
                    "Pengikut IG": st.column_config.NumberColumn("📱 IG Followers", format="%d"),
                },
            )

        with right:
            chart_title("🧾", "Detail Destinasi Dipilih")
            option_map = {
                f"{row['Nama Tempat']} | {row['Lokasi']} | {row['Kategori']} | index {idx}": idx
                for idx, row in search_df.iterrows()
            }
            selected_label = st.selectbox("Pilih destinasi", list(option_map.keys()))
            selected_row = search_df.loc[option_map[selected_label]]

            harga_value = int(selected_row["Harga Tiket"]) if pd.notna(selected_row["Harga Tiket"]) else 0
            harga_text = "Gratis" if harga_value == 0 else f"Rp {fmt_num(harga_value)}"
            fasilitas_text = selected_row.get("Fasilitas", "")
            review_text = selected_row.get("Review", "")

            st.markdown(
                f"""
                <div class="destination-card">
                    <h3>{escape(str(selected_row['Nama Tempat']))}</h3>
                    <div class="pill-row">
                        <span class="pill">📍 {escape(str(selected_row['Lokasi']))}</span>
                        <span class="pill">🏷️ {escape(str(selected_row['Kategori']))}</span>
                        <span class="pill">⭐ {float(selected_row['Rating']):.1f}</span>
                        <span class="pill">💰 {escape(harga_text)}</span>
                    </div>
                    <div class="detail-box">
                        <b>Jumlah Review:</b> {fmt_num(selected_row['Jumlah Review'])}<br>
                        <b>Pengikut Instagram:</b> {fmt_num(selected_row['Pengikut IG'])}<br>
                        <b>Fasilitas:</b> {escape(str(fasilitas_text))}<br><br>
                        <b>Ulasan:</b><br>{escape(str(review_text))}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        chart_title("📊", "Sebaran Kategori dari Hasil Pencarian")
        cat_search = search_df["Kategori"].value_counts().reset_index()
        cat_search.columns = ["Kategori", "Jumlah"]
        fig_search = px.bar(
            cat_search,
            x="Kategori",
            y="Jumlah",
            color="Kategori",
            color_discrete_map=CATEGORY_COLORS,
            text="Jumlah",
        )
        fig_search.update_traces(textposition="outside", marker_line_width=0)
        fig_search.update_layout(
            **PLOTLY_LAYOUT,
            height=360,
            showlegend=False,
            xaxis_title="Kategori",
            yaxis_title="Jumlah Destinasi",
        )
        show_chart(fig_search)


# ============================================================
# PAGE: TENTANG DATASET
# ============================================================
elif selected_menu == "Tentang Dataset":
    st.markdown(
        """
        <div class="page-header">
            <h1>🗄️ Tentang Dataset</h1>
            <p>Informasi struktur data, jumlah atribut, fungsi kolom, serta ringkasan kualitas data destinasi wisata Lampung.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    d1, d2, d3, d4 = st.columns(4)
    with d1:
        st.metric("Jumlah Baris", fmt_num(len(df)))
    with d2:
        st.metric("Jumlah Kolom", fmt_num(len(df.columns) - 1))
    with d3:
        st.metric("Lokasi Unik", fmt_num(df["Lokasi"].nunique()))
    with d4:
        st.metric("Kategori Unik", fmt_num(df["Kategori"].nunique()))

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📌 Fungsi Setiap Kolom")
    st.markdown(
        """
        <table class="dataset-table">
            <tr><th>Kolom</th><th>Keterangan</th></tr>
            <tr><td>Nama Tempat</td><td>Nama destinasi wisata yang tercatat pada dataset.</td></tr>
            <tr><td>Lokasi</td><td>Kabupaten atau kota tempat destinasi berada.</td></tr>
            <tr><td>Kategori</td><td>Jenis destinasi seperti alam, buatan, budaya, kuliner, cafe, atau hotel.</td></tr>
            <tr><td>Rating</td><td>Nilai penilaian destinasi yang digunakan untuk melihat kualitas persepsi pengunjung.</td></tr>
            <tr><td>Jumlah Review</td><td>Total ulasan pengunjung yang menjadi indikator popularitas.</td></tr>
            <tr><td>Harga Tiket</td><td>Biaya masuk destinasi dalam rupiah.</td></tr>
            <tr><td>Pengikut IG</td><td>Jumlah pengikut Instagram sebagai indikator daya tarik media sosial.</td></tr>
            <tr><td>Fasilitas</td><td>Informasi fasilitas yang tersedia pada destinasi.</td></tr>
            <tr><td>Review</td><td>Ringkasan ulasan atau komentar pengunjung.</td></tr>
        </table>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        chart_title("📊", "Jumlah Data per Kategori")
        ds_cat = df["Kategori"].value_counts().reset_index()
        ds_cat.columns = ["Kategori", "Jumlah"]
        fig_ds = px.bar(ds_cat, x="Kategori", y="Jumlah", color="Kategori", color_discrete_map=CATEGORY_COLORS, text="Jumlah")
        fig_ds.update_traces(textposition="outside", marker_line_width=0)
        fig_ds.update_layout(**PLOTLY_LAYOUT, height=360, showlegend=False, xaxis_title="Kategori", yaxis_title="Jumlah")
        show_chart(fig_ds)
    with c2:
        chart_title("💰", "Komposisi Segment Harga")
        ds_price = df["Segment Harga"].value_counts().reset_index()
        ds_price.columns = ["Segment Harga", "Jumlah"]
        fig_price = px.pie(ds_price, values="Jumlah", names="Segment Harga", hole=0.52, color_discrete_sequence=PASTEL_SET)
        fig_price.update_traces(textinfo="label+percent", marker=dict(line=dict(color="#FFFFFF", width=2)))
        fig_price.update_layout(**PLOTLY_LAYOUT, height=360, showlegend=False)
        show_chart(fig_price)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 👀 Pratinjau Data")
    st.dataframe(df.drop(columns=["Segment Harga"], errors="ignore").head(20), use_container_width=True, hide_index=True, height=420)


# ============================================================
# PAGE: DATA DETAIL
# ============================================================
elif selected_menu == "Data Detail":
    st.markdown(
        """
        <div class="page-header">
            <h1>📋 Data Detail Destinasi</h1>
            <p>Tabel interaktif lengkap. Gunakan pencarian dan pilihan kolom untuk melihat data secara lebih rapi.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<div class='hint-card'>💡 Gunakan kotak pencarian dan pilihan kolom untuk menyesuaikan data. Tombol download akan menyimpan data yang sedang tampil.</div>", unsafe_allow_html=True)

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.metric("Data Ditampilkan", f"{len(df_filtered)} baris")
    with k2:
        st.metric("Lokasi Unik", f"{df_filtered['Lokasi'].nunique()}")
    with k3:
        st.metric("Kategori Unik", f"{df_filtered['Kategori'].nunique()}")
    with k4:
        gratis = len(df_filtered[df_filtered["Harga Tiket"] == 0])
        st.metric("Destinasi Gratis", f"{gratis}")

    st.markdown("<br>", unsafe_allow_html=True)

    search = st.text_input("🔎 Cari Nama Tempat", placeholder="Ketik nama destinasi...")
    df_display = df_filtered.copy()
    if search:
        df_display = df_display[df_display["Nama Tempat"].str.contains(search, case=False, na=False)]

    all_cols = ["Nama Tempat", "Lokasi", "Kategori", "Rating", "Jumlah Review", "Harga Tiket", "Segment Harga", "Pengikut IG", "Fasilitas", "Review"]
    display_cols = st.multiselect(
        "📋 Pilih Kolom Ditampilkan",
        all_cols,
        default=["Nama Tempat", "Lokasi", "Kategori", "Rating", "Jumlah Review", "Harga Tiket"],
    )

    if display_cols:
        st.dataframe(
            df_display[display_cols].reset_index(drop=True),
            use_container_width=True,
            hide_index=True,
            height=600,
            column_config={
                "Rating": st.column_config.NumberColumn("⭐ Rating", format="%.1f"),
                "Jumlah Review": st.column_config.NumberColumn("📝 Review", format="%d"),
                "Harga Tiket": st.column_config.NumberColumn("💰 Harga", format="Rp %d"),
                "Pengikut IG": st.column_config.NumberColumn("📱 IG Followers", format="%d"),
            },
        )

        csv_data = df_display[display_cols].to_csv(index=False).encode("utf-8")
        st.download_button(
            "📥 Download Data (CSV)",
            csv_data,
            "wisata_lampung_filtered.csv",
            "text/csv",
            use_container_width=True,
        )
    else:
        st.warning("Pilih minimal 1 kolom untuk ditampilkan.")


render_footer()
