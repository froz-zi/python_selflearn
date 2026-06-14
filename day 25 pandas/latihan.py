import pandas as pd
from pathlib import Path

# File CSV berada satu folder di atas folder script.
csv_path = Path(__file__).resolve().parent.parent / "ai_data.csv"
df = pd.read_csv(csv_path)

print("=== First Five Rows ===")
print(df.head())

print("\n=== Last Five Rows ===")
print(df.tail())

# ai_data.csv tidak memiliki kolom "title"; gunakan Primary_Use_Case.
print("\n=== Primary_Use_Case Column as Pandas Series ===")
title = df["Primary_Use_Case"]
print(title)

hasil_filter = df[
    (df["Year_of_Study"].str.contains("Freshman", case=False, na=False)) &
    (df["Primary_Use_Case"].str.contains("Copywriting", case=False, na=False)) &
    (df["Prompt_Engineering_Skill"].str.contains("Beginner", case=False, na=False))
]

print("=== Freshman, Copywriting, dan Beginner ===")
print(hasil_filter.to_string(index=False))
print(f"\nJumlah data ditemukan: {len(hasil_filter)}")
