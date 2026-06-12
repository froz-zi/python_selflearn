from datetime import datetime

# 1. Dapatkan hari, bulan, tahun, jam, menit, dan timestamp saat ini
now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print("Hari:", day)
print("Bulan:", month)
print("Tahun:", year)
print("Jam:", hour)
print("Menit:", minute)
print("Timestamp:", timestamp)


# 2. Format tanggal sekarang: "%m/%d/%Y, %H:%M:%S"
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted date:", formatted_date)


# 3. Hari ini tanggal 5 Desember 2019. Ubah string waktu ini menjadi waktu
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")

print("Date object:", date_object)


# 4. Hitung selisih waktu antara sekarang dan tahun baru
new_year = datetime(year + 1, 1, 1)

time_left_for_new_year = new_year - now
print("Time left for New Year:", time_left_for_new_year)


# 5. Hitung selisih waktu antara 1 Januari 1970 dengan sekarang
epoch = datetime(1970, 1, 1)

time_since_epoch = now - epoch
print("Time since 1 January 1970:", time_since_epoch)


# 6. Untuk apa menggunakan modul datetime?
print("Modul datetime digunakan untuk:")
print("- Mengambil tanggal dan waktu saat ini")
print("- Membuat timestamp aktivitas aplikasi")
print("- Menghitung selisih waktu")
print("- Format tanggal dan waktu")
print("- Analisis data berdasarkan waktu")