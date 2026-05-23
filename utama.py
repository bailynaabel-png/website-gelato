import streamlit as st
import pandas as pd
import os

# ==========================
# KONFIGURASI WEBSITE
# ==========================
st.set_page_config(
    page_title="D'Gelatos 🍦",
    page_icon="🍨",
    layout="wide"
)

# ==========================
# STYLE / BACKGROUND
# ==========================
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(
135deg,
#ffd6e8,
#fff3c7,
#dff6ff
);
}

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

h1{
text-align:center;
color:#ff4d6d;
font-size:60px;
}

div[data-testid="column"]{
background:white;
padding:15px;
border-radius:20px;
box-shadow:0px 6px 15px rgba(0,0,0,0.12);
}

</style>
""", unsafe_allow_html=True)

# ==========================
# BANNER
# ==========================
if os.path.exists("D'gelato.png"):
    st.image("D'gelato.png", use_container_width=True)

# ==========================
# JUDUL
# ==========================
st.title("🍦 D'Gelatos")
st.caption("Sweet • Fresh • Happiness in Every Scoop ✨")

st.divider()

# ==========================
# BACA CSV
# ==========================
df = pd.read_csv("data-gelato.csv")

kategori_list = df["kategori"].unique()

for kat in kategori_list:

    st.header(f"🍨 {kat}")

    data_kat = df[df["kategori"] == kat]

    cols = st.columns(3)

    for index, row in data_kat.reset_index().iterrows():

        with cols[index % 3]:

            # FOTO
            if os.path.exists(row["foto"]):
                st.image(row["foto"], use_container_width=True)

            # NAMA
            st.subheader(row["nama"])

            # HARGA
            st.markdown(f"### 💸 Rp {row['harga']}")

            # STATUS
            st.success(f"Status: {row['status']}")

            # TOMBOL ORDER (FIX NO ERROR)
            if st.button(
                f"🛒 Order {row['nama']}",
                key=f"order_{kat}_{index}"
            ):
                st.success("Pesanan ditambahkan!")

    st.divider()

# ==========================
# FOOTER
# ==========================
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
