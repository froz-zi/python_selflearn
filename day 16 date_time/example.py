import datetime

print(dir(datetime))


from datetime import datetime

now = datetime.now()
print(now)  # 08-07-2021 07:34:46.549883
day = now.day  # 8
month = now.month  # 7
year = now.year  # 2021
hour = now.hour  # 7
minute = now.minute  # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')


### Memformat Output Tanggal Menggunakan *strftime*
print("====")
from datetime import datetime
new_year = datetime(2020, 1, 1)
# print(new_year)  # 01-01-2020 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)  # 1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0


# Memformat tanggal waktu menggunakan metode *strftime* dan dokumentasinya dapat ditemukan .

# ```python
from datetime import datetime
# tanggal dan waktu saat ini
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)  # waktu: 18:21:40
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/hh/YY format H:M:S
print("time one:", time_one)  # waktu pertama: 28/06/2022, 18:21:40
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# format dd/mm/YY H:M:S
print("time two:", time_two)  # waktu kedua: 28/06/2022, 18:21:40


jam = now.strftime("%d, %m, %y" )
jam2 = ("%d")
print(jam)


sekarang = datetime.now()

hari = now.day

print(hari)
