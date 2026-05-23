import streamlit as st
import pandas as pd

st.set_page_config(page_title="Katalog Gelato", layout="wide")

st.title("🍦 Katalog Gelato")
st.divider()

try:
    df = pd.read_csv("data-gelato.csv")

    daftar_kategori = df['kategori'].unique()

    for kat in daftar_kategori:
        st.header(f"🍨 Rasa {kat}")

        data_per_kat = df[df['kategori'] == kat]

        cols = st.columns(3)

        for index, row in data_per_kat.reset_index().iterrows():

            with cols[index % 3]:

                st.subheader(row['nama'])
                st.markdown(f"### Rp {row['harga']}")
                st.write(f"Status: {row['status']}")
                st.write(f"Foto: {row['foto']}")

        st.divider()

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
