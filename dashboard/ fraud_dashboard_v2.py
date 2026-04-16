import streamlit as st
import pandas as pd
import os
import time

st.set_page_config(page_title="Fraud Dashboard", layout="wide")
st.title("🛡️ Real-Time Fraud Detection Dashboard")

path = "stream_data/realtime_output/"

# Fungsi untuk mengecek dan memuat data
def load_data():
    # Cek apakah folder ada dan ada isinya (file .parquet)
    if os.path.exists(path) and any(f.endswith('.parquet') for f in os.listdir(path)):
        try:
            return pd.read_parquet(path)
        except:
            return None
    return None

# Tempat penampung dashboard agar bisa di-refresh
placeholder = st.empty()

while True:
    df = load_data()
    
    with placeholder.container():
        if df is not None and not df.empty:
            # Baris Metrik
            col1, col2 = st.columns(2)
            col1.metric("Total Transaksi", len(df))
            col2.metric("Total Fraud", len(df[df["status"] == "FRAUD"]), delta_color="inverse")

            # Tabel
            st.subheader("📋 10 Transaksi Terakhir")
            st.dataframe(df.tail(10), use_container_width=True)

            # Grafik
            st.subheader("📊 Statistik Status")
            st.bar_chart(df["status"].value_counts())
        else:
            st.info("⌛ Menunggu data dari Spark Streaming... Pastikan Kafka dan Spark sudah jalan.")
    
    # Tunggu 5 detik sebelum refresh data terbaru
    time.sleep(5)