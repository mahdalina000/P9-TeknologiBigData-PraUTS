# 🚦 Smart City Traffic Monitoring & AI Prediction

---

## 📝 Deskripsi Proyek
Proyek ini mengimplementasikan sistem monitoring lalu lintas real-time yang mensimulasikan sensor kendaraan di tiga area berbeda (Area A, B, dan C). Sistem ini menggunakan **Apache Spark** untuk pemrosesan data besar dan **Streamlit** untuk visualisasi dashboard yang dilengkapi dengan model **AI (Linear Regression)** untuk memprediksi kepadatan kendaraan di masa depan.

## 🚀 Fitur Utama
- **Real-time Data Ingestion**: Menggunakan PySpark untuk mensimulasikan data dan menyimpan ke format **Parquet** secara incremental.
- **AI Prediction**: Model Machine Learning untuk memprediksi jumlah kendaraan berdasarkan input jam.
- **Interactive Dashboard**: Visualisasi data interaktif menggunakan Plotly yang menampilkan distribusi kendaraan per area.
- **Efficient Storage**: Implementasi penyimpanan berbasis kolom (Parquet) untuk efisiensi query Big Data.

## 📁 Struktur Folder Proyek
```text
bigdata-project/
├── dashboard/
│   └── dashboard_230104040127.py  # Script UI Dashboard (Streamlit)
├── scripts/
│   └── main_uts_230104040127.py    # Script Processing (Spark Ingestion)
├── traffic_data/                   # Folder Output Data (Format Parquet)
├── venv/                           # Virtual Environment Python
└── README.md                       # Dokumentasi Proyek
