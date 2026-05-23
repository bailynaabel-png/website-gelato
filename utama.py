import streamlit as st
import pandas as pd
import os

# KONFIGURASI HALAMAN
st.set_page_config(
    page_title="D'Gelatos 🍦",
    page_icon="🍨",
    layout="wide"
)

# STYLE WEBSITE
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(
135deg,
#ffd6e8,
#fff0c9,
#d8f3ff
);
}

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

h1{
text-align:center;
color:white;
font-size:65px;
text-shadow:3px 3px 12px #ff4d6d;
}

h2,h3{
color:#ff4d6d;
}

.stButton>button{
background:#ff4d6d;
color:white;
border:none;
border-radius:18px;
padding:10px 18px;
font-weight:bold;
}

.card{
background:white;
padding:20px;
border-radius:25px;
box-shadow:0px 8px 18px rgba(0,0,0,0.15);
margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# BANNER CANVA
if os.path.exists("banner.png"):
    st.image("banner.png", use_container_width=True)

# JUDUL
st.markdown("""
<h1>🍦 D'Gelatos 🍓</h1>
<h3 style='text-align:center;color:white;'>

Sweet • Fresh • Happiness in Every Scoop ✨

</h3>
""", unsafe_allow_html=True)

st.divider()

# BACA CSV
df = pd.read_csv("data-gelato.csv")

kategori_unik = df['kategori'].unique()

# PRODUK
for kat in kategori_unik:

    st.header(f"🍨 {kat}")

    data_kat = df[df['kategori']==kat]

    cols = st.columns(3)

    for index, row in data_kat.reset_index().iterrows():

        with cols[index % 3]:

            st.markdown("<div class='card'>", unsafe_allow_html=True)

            if os.path.exists(row['foto']):
                st.image(row['foto'], use_container_width=True)

            st.subheader(row['nama'])

            st.markdown(
                f"<h3>💸 Rp {row['harga']}</h3>",
                unsafe_allow_html=True
            )

            st.success(f"Status: {row['status']}")

            st.button(
                f"🛒 Order {row['nama']}",
                key=index
            )

            st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# FOOTER
st.subheader("📍 Hubungi Kami")

col1,col2 = st.columns(2)

with col1:

    st.info("""
🏪 **D'Gelatos**

Yogyakarta, Indonesia
""")

with col2:

    no_hp = "6281234567890"

    pesan = "Halo D'Gelatos! Saya ingin memesan gelato 🍦"

    link = f"https://wa.me/{no_hp}?text={pesan.replace(' ','%20')}"

    st.link_button(
        "📱 Pesan via WhatsApp",
        link
    )

st.caption("© 2026 D'Gelatos — Sweetness Delivered Daily 🍓")
