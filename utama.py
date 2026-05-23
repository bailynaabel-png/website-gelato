import streamlit as st
import pandas as pd
import os

# Konfigurasi halaman
st.set_page_config(
    page_title="D'Gelato 🍦",
    layout="wide"
)

# Judul website
st.title("🍦 D'Gelato")
st.caption("Sweet • Fresh • Happiness in Every Scoop ✨")
st.divider()

# Baca data CSV
df = pd.read_csv("data-gelato.csv")

# Ambil kategori unik
kategori_unik = df['kategori'].unique()

for kat in kategori_unik:

    st.header(f"🍨 {kat}")

    data_kat = df[df['kategori'] == kat]

    cols = st.columns(3)

    for index, row in data_kat.reset_index().iterrows():

        with cols[index % 3]:

            # tampilkan foto
            if os.path.exists(row['foto']):
                st.image(row['foto'], use_container_width=True)

            st.subheader(row['nama'])

            st.markdown(f"### 💸 Rp {row['harga']}")

            st.success(f"Status: {row['status']}")

    st.divider()

# Footer
st.subheader("📍 Hubungi Kami")

st.write("""
**D'Gelato 🍦**

Yogyakarta, Indonesia

📱 WhatsApp: 08123456789
""")

st.caption("© 2026 D'Gelato — All Rights Reserved")
