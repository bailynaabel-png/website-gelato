import streamlit as st
import pandas as pd
import os

# Konfigurasi
st.set_page_config(
    page_title="D'Gelatos 🍦",
    page_icon="🍨",
    layout="wide"
)

# Background
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg,#ffd6e8,#fff3c7,#dff6ff);
}

h1{
text-align:center;
color:#ff4d6d;
}

</style>
""", unsafe_allow_html=True)

# Banner
if os.path.exists("D'gelato.png"):
    st.image("D'gelato.png", use_container_width=True)

# Judul
st.title("🍦 D'Gelatos")
st.caption("Sweet • Fresh • Happiness in Every Scoop ✨")

st.divider()

# Baca data CSV
df = pd.read_csv("data-gelato.csv")

kategori = df["kategori"].unique()

for kat in kategori:

    st.header(f"🍨 {kat}")

    data_kat = df[df["kategori"] == kat]

    cols = st.columns(3)

    for index, row in data_kat.reset_index().iterrows():

        with cols[index % 3]:

            if os.path.exists(row["foto"]):
                st.image(row["foto"], use_container_width=True)

            st.subheader(row["nama"])

            st.markdown(f"### 💸 Rp {row['harga']}")

            st.success(f"Status: {row['status']}")

            tombol = st.button(
                f"🛒 Order {row['nama']}",
                key=f"btn{index}"
            )

    st.divider()

# Footer
st.subheader("📍 Hubungi Kami")

col1, col2 = st.columns(2)

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
