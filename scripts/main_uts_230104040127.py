import findspark
findspark.init("/opt/spark")

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, rand, round, current_timestamp, hour
import os
import time

# Inisialisasi Spark
spark = SparkSession.builder \
    .appName("SmartCityTraffic_Mahdalina") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Pastikan Path Absolut Benar
base_path = "/home/mahdalina/traffic_project/data"

print("=== SENSOR TRAFFIC ACTIVE ===")
print(f"Saving data to: {base_path}/traffic")

try:
    while True:
        # Simulasi 3 Area CCTV
        data = [("AreaA",), ("AreaB",), ("AreaC",)]
        df = spark.createDataFrame(data, ["area"])

        # Generate data random: kendaraan 10-100, jam, dan waktu
        df_final = df.withColumn("vehicle_count", round(rand() * 90 + 10).cast("int")) \
                     .withColumn("timestamp", current_timestamp()) \
                     .withColumn("hour", hour(current_timestamp()))

        # Simpan ke Parquet
        df_final.write.mode("append").parquet(f"{base_path}/traffic")
        
        print(f"[{time.strftime('%H:%M:%S')}] Batch Data Tersimpan ke Parquet...")
        time.sleep(5) # Kirim tiap 5 detik

except KeyboardInterrupt:
    print("\nSimulasi Berhenti.")
    spark.stop()
