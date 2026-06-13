import requests
import pandas as pd
import json
import re
from bs4 import BeautifulSoup
from io import StringIO

headers = {
    "User-Agent": "Mozilla/5.0"
}


def clean_text(text):
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def save_json(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# =====================================================
# 1. Scrape BU Facts & Stats
# =====================================================

def scrape_bu_facts():
    url = "http://www.bu.edu/president/boston-university-facts-stats/"

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    facts = []

    # Ambil heading dan isi angka yang berdekatan
    headings = soup.find_all(["h2", "h3", "h4", "li"])

    for tag in headings:
        text = clean_text(tag.get_text(" "))

        if text:
            facts.append(text)

    data = {
        "source": url,
        "facts": facts
    }

    save_json(data, "bu_facts_stats.json")
    print("File bu_facts_stats.json berhasil dibuat")


# =====================================================
# 2. Extract UCI dataset table to JSON
# =====================================================

def scrape_uci_datasets():
    old_url = "https://archive.ics.uci.edu/ml/datasets.php"
    new_url = "https://archive.ics.uci.edu/datasets"

    try:
        # Coba pakai URL lama dulu
        tables = pd.read_html(old_url)

        if len(tables) > 0:
            df = tables[0]
            data = df.to_dict(orient="records")
            save_json(data, "uci_datasets.json")
            print("File uci_datasets.json berhasil dibuat dari URL lama")
            return

    except Exception:
        print("URL lama UCI gagal, mencoba URL baru...")

    # Fallback ke URL baru
    response = requests.get(new_url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    datasets = []

    dataset_titles = soup.find_all("h2")

    for title in dataset_titles:
        name = clean_text(title.get_text())

        parent = title.find_parent()

        if parent:
            text = clean_text(parent.get_text(" "))
        else:
            text = name

        datasets.append({
            "name": name,
            "raw_info": text
        })

    save_json(datasets, "uci_datasets.json")
    print("File uci_datasets.json berhasil dibuat dari URL baru")


# =====================================================
# 3. Scrape Wikipedia Presidents table
# =====================================================

def scrape_us_presidents():
    url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    html_data = StringIO(response.text)

    tables = pd.read_html(html_data)

    # Ambil tabel terbesar, biasanya ini tabel daftar presiden
    presidents_table = max(tables, key=lambda table: table.shape[0])

    # Jika kolomnya bertingkat / MultiIndex, ubah jadi kolom biasa
    if isinstance(presidents_table.columns, pd.MultiIndex):
        presidents_table.columns = [
            " ".join([str(col) for col in column if str(col) != "nan"])
            for column in presidents_table.columns
        ]
    else:
        presidents_table.columns = [str(col) for col in presidents_table.columns]

    # Bersihkan nama kolom
    presidents_table.columns = [
        clean_text(col) for col in presidents_table.columns
    ]

    # Bersihkan isi data
    presidents_table = presidents_table.fillna("")

    for column in presidents_table.columns:
        presidents_table[column] = presidents_table[column].astype(str).apply(clean_text)

    data = presidents_table.to_dict(orient="records")

    save_json(data, "us_presidents.json")

    print("File us_presidents.json berhasil dibuat")


# =====================================================
# Jalankan semua fungsi
# =====================================================

scrape_bu_facts()
scrape_uci_datasets()
scrape_us_presidents()