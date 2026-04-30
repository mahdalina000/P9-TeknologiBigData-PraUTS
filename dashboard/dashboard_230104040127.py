import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np
import os

st.set_page_config(page_title="Traffic AI Dashboard", layout="wide")

st.title("🚦 Smart City Traffic Monitoring & Prediction")
st.markdown("---")

# Path ke data parquet
data_path = "/home/mahdalina/traffic_project/data/traffic"

if os.path.exists(data_path):
    # Baca data menggunakan Pandas (untuk visualisasi cepat)
    # Catatan: Di Big Data asli kita pakai Spark, tapi untuk UI Streamlit 
    # lebih ringan dikonversi ke Pandas.
    df = pd.read_parquet(data_path)
    
    # --- BAGIAN PREDIKSI AI (LINEAR REGRESSION) ---
    st.sidebar.header("AI Prediction Settings")
    input_hour = st.sidebar.slider("Pilih Jam untuk Prediksi Kepadatan", 0, 23, 12)
    
    # Siapkan Model
    X = df[['hour']].values
    y = df['vehicle_count'].values
    model = LinearRegression()
    model.fit(X, y)
    
    # Prediksi
    prediction = model.predict([[input_hour]])
    
    # --- TAMPILAN METRIK ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Data Sensor", len(df))
    col2.metric("Rata-rata Kendaraan", f"{int(df['vehicle_count'].mean())} Unit")
    col3.metric(f"Prediksi Jam {input_hour}:00", f"{int(prediction[0])} Kendaraan", delta="AI Predicted")

    # --- GRAFIK PLOTLY ---
    st.subheader("Distribusi Kepadatan per Area")
    fig = px.box(df, x="area", y="vehicle_count", color="area", points="all")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Tren Kepadatan (Real-time)")
    fig_line = px.line(df.sort_values("timestamp"), x="timestamp", y="vehicle_count", color="area")
    st.plotly_chart(fig_line, use_container_width=True)

else:
    st.warning("Menunggu data dari sensor... Silakan jalankan script main_uts dulu!")
