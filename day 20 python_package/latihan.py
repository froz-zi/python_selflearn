import requests
from bs4 import BeautifulSoup
import re

url = "https://whello.id/tips-digital-marketing/platform-blog/?srsltid=AfmBOopuXFnelbcd8vy-W7ttHvIQasjAUQmgOkIr-YOQv9tKJczpLhTk"

response = requests.get(url)


url = "https://whello.id/tips-digital-marketing/platform-blog/?srsltid=AfmBOopuXFnelbcd8vy-W7ttHvIQasjAUQmgOkIr-YOQv9tKJczpLhTk"

# 1. Ambil isi halaman web
response = requests.get(url)
html = response.text

# 2. Ubah HTML menjadi teks
soup = BeautifulSoup(html, "html.parser")

# 3. Ambil teks utama dari halaman
text = soup.get_text(separator=" ")

# 4. Ubah ke huruf kecil
text = text.lower()

# 5. Ambil hanya kata a-z dan huruf Indonesia
words = re.findall(r"[a-zA-Z]+", text)

# 6. Kata umum yang mau diabaikan
stop_words = [
    "dan", "yang", "di", "ke", "dari", "ini", "itu", "untuk",
    "dengan", "atau", "sebagai", "adalah", "pada", "dalam",
    "oleh", "juga", "lebih", "akan", "dapat", "saat", "telah",
    "menjadi", "bagi", "ada", "secara", "sangat"
]

# 7. Hitung frekuensi kata tanpa Counter
word_counts = {}

for word in words:
    if word not in stop_words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

# 8. Urutkan dari yang paling sering
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# 9. Ambil 10 teratas
top_10 = sorted_words[:10]

# 10. Tampilkan hasil
print(top_10)# ai


# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find : the min, max, mean, median, standard deviation of cats' weight in metric units. the min, max, mean, median, standard deviation of cats' lifespan in years. Create a frequency table of country and breed of cats
import requests
import numpy as np
import pandas as pd

cats_api = "https://api.thecatapi.com/v1/breeds"

response = requests.get(cats_api)
data = response.json()

# Untuk menyimpan hasil yang sudah dibersihkan
cats_data = []

for cat in data:
    breed = cat["name"]
    country = cat["origin"]
    
    weight_metric = cat["weight"]["metric"]   # contoh: "3 - 5"
    life_span = cat["life_span"]              # contoh: "14 - 15"
    
    # Pisahkan berat minimum dan maksimum
    weight_min, weight_max = weight_metric.split(" - ")
    weight_min = float(weight_min)
    weight_max = float(weight_max)
    
    # Ambil nilai tengah berat
    weight_avg = (weight_min + weight_max) / 2
    
    # Pisahkan lifespan minimum dan maksimum
    life_min, life_max = life_span.split(" - ")
    life_min = float(life_min)
    life_max = float(life_max)
    
    # Ambil nilai tengah lifespan
    life_avg = (life_min + life_max) / 2
    
    
    cats_data.append({
        
        "breed": breed,
        "country": country,
        "weight_min": weight_min,
        "weight_max": weight_max,
        "weight_avg": weight_avg,
        "life_min": life_min,
        "life_max": life_max,
        "life_avg": life_avg
        
    })




df = pd.DataFrame(cats_data)
weight_stats = {
    "min": df["weight_avg"].min(),
    "max": df["weight_avg"].max(),
    "mean": df["weight_avg"].mean(),
    "median": df["weight_avg"].median(),
    "standard deviation": df["weight_avg"].std()
}

print("Statistik Berat Kucing dalam Metric Unit")
print("Min:", weight_stats["min"])
print("Max:", weight_stats["max"])
print("Mean:", weight_stats["mean"])
print("Median:", weight_stats["median"])
print("Standard Deviation:", weight_stats["standard deviation"])

print(df.head())#ai


     