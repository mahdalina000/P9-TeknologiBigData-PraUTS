from kafka import KafkaProducer
import json, time, random

# Inisialisasi Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🚀 Kafka Producer jalan... Mengirim data transaksi.")

while True:
    data = {
        "nama": random.choice(["Andi", "Budi", "Citra", "Mahdalina"]),
        "rekening": str(random.randint(100000, 999999)),
        "jumlah": random.randint(100000, 100000000),
        "lokasi": random.choice(["Jakarta", "Luar Negeri"])
    }
    producer.send("bank_topic", value=data)
    print(f"Terkirim: {data}")
    time.sleep(2)