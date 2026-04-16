# ==========================================================
# VISUALIZATION LAYER - DASHBOARD VERSION
# Big Data Dashboard
# ==========================================================
import findspark
findspark.init("/opt/spark")

import os
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-17-openjdk-amd64'

from pyspark.sql import SparkSession
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import os

# --- Tambahan untuk Tampilan Streamlit ---
st.set_page_config(page_title="Fraud Analytics Dashboard", layout="wide")
st.title("📊 Real-Time Fraud Analytics Dashboard")
st.markdown(f"**User:** mahdalina | **Project:** Big Data Pipeline")

print("========================================")
print("       VISUALIZATION LAYER STARTED      ")
print("========================================")

# =========================
# INITIALIZE SPARK
# =========================
spark = SparkSession.builder \
    .appName("VisualizationLayer") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# =========================
# LOAD CLEAN DATA
# =========================
st.sidebar.header("Data Status")
print("Loading Clean Parquet Data...")

# Membaca data parquet
df = spark.read.parquet("data/clean/parquet/")

total_records = df.count()
print("Total Records:", total_records)
st.sidebar.metric("Total Records Processed", f"{total_records:,}")

print("----------------------------------------")

# =========================
# CREATE REPORT FOLDER
# =========================
if not os.path.exists("reports"):
    os.makedirs("reports")

# =========================
# CATEGORY REVENUE
# =========================
print("Generating Category Revenue Chart...")

df = df.withColumn(
    "total_amount",
    df.price * df.quantity
)

category_df = df.groupBy("category") \
    .sum("total_amount") \
    .toPandas()

category_df = category_df.sort_values(
    "sum(total_amount)", 
    ascending=False
)

# Membuat Plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(
    category_df["category"], 
    category_df["sum(total_amount)"],
    color='skyblue'
)

plt.xticks(rotation=45)
plt.title("Revenue per Category")
plt.ylabel("Total Revenue")
plt.tight_layout()

# Simpan ke folder reports
plt.savefig("reports/category_revenue.png")
print("Visualization saved to reports/category_revenue.png")

# TAMPILKAN DI STREAMLIT
st.subheader("1. Revenue Analysis by Category")
st.pyplot(fig)

# Tambahkan tabel data di bawahnya untuk detail
with st.expander("Lihat Detail Data Tabel"):
    st.write(category_df)

# =========================
# STOP SPARK
# =========================
spark.stop()

print("========================================")
print("       VISUALIZATION COMPLETED          ")
print("========================================")