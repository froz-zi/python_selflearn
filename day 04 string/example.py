# Komentar satu baris
letter = 'P'  # Sebuah string dapat berupa satu karakter atau sekumpulan teks
print(letter)  # P
print(len(letter))  # 1
greeting = 'Hello, World!'  # String dapat berupa tanda kutip tunggal atau ganda, "Halo, Dunia!"
print(greeting)  # Halo Dunia!
print(len(greeting))  # 13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

# String Multibaris
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
# Cara lain untuk melakukan hal yang sama
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# Penggabungan String
first_name = 'Vincen'
last_name = 'babi'
space = ' '
full_name = first_name + space + last_name
print(full_name)  # Keterbukaan Informasi
# Memeriksa panjang string menggunakan fungsi bawaan len()
print(len(first_name))  # 8
print(len(last_name))  # 7
print(len(first_name) > len(last_name))  # BENAR
print(len(full_name))  # 15

# Membongkar karakter
language = 'Pythond'
a, b, c, d, e, f , g= language  # membongkar karakter urutan ke dalam variabel
print(a)  # P
print(b)  # kamu
print(c)  # T
print(d)  # H
print(e)  # Hai
print(f)  # N
print(g)

# Mengakses karakter dalam string berdasarkan indeks
language = 'Python'
first_letter = language[0]
print(first_letter)  # P
second_letter = language[1]
print(second_letter)  # kamu
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # n

# Jika kita ingin memulai dari ujung kanan kita bisa menggunakan pengindeksan negatif.-1 adalah indeks terakhir
language = 'Python'
last_letter = language[-1]
print(last_letter)  # N
second_last = language[-2]
print(second_last)  # Hai

# Mengiris

language = 'Python'
# dimulai dari indeks nol dan hingga 3 tetapi tidak termasuk 3
first_three = language[0:3]
last_three = language[3:6]
print(last_three)  # sayang
# Cara lain
last_three = language[-3:]
print(last_three)  # sayang
last_three = language[3:]
print(last_three)  # sayang

# Melewatkan karakter saat memisahkan string Python
language = 'Python'
pto = language[0:6:2]
print(pto)  # pto

# Urutan pelarian
print('I hope every one enjoying the python challenge.\nDo you ?')  # jeda baris
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)')  # Untuk menulis garis miring ke belakang
print('In every programming language it starts with \"Hello, World!\"')

# Metode String
# capitalize(): Mengonversi karakter pertama string menjadi Huruf Kapital

challenge = 'thirty days of python'
print(challenge.capitalize())  # 'Tiga puluh hari ular piton'

# count(): mengembalikan kemunculan substring dalam string, count(substring, start=.., end=..)

challenge = 'thirty days of python'
print(challenge.count('y'))  # 3
print(challenge.count('y', 7, 14))  # 1
print(challenge.count('th'))  # 2`

# endwith(): Memeriksa apakah string diakhiri dengan akhiran tertentu

challenge = 'thirty days of python'
print(challenge.endswith('on'))  # True
print(challenge.endswith('tion'))  # False

# expandtabs(): Mengganti karakter tab dengan spasi, ukuran tab default adalah 8. Dibutuhkan argumen ukuran tab

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())  # 'tiga puluh hari ular piton'
print(challenge.expandtabs(10))  # 'tiga puluh hari ular piton'

# find(): Mengembalikan indeks kemunculan substring pertama

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0

# format() memformat string menjadi keluaran yang lebih bagus
first_name = 'Vincen'
last_name = 'babi'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(
    first_name, last_name, job, country)
print(sentence)  # Saya Vincen babi.Saya guru.Saya tinggal di Finlandia.

radius = 10
pi = 3.14
area = pi  # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result)  # Luas lingkaran dengan 10 adalah 314,0

# indeks(): Mengembalikan indeks substring
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0

# isalnum(): Memeriksa karakter alfanumerik

challenge = 'ThirtyDaysPython'
print(challenge.isalnum())  # BENAR

challenge = '30DaysPython'
print(challenge.isalnum())  # BENAR

challenge = 'thirty days of python'
print(challenge.isalnum())  # PALSU

challenge = 'thirty days of python 2019'
print(challenge.isalnum())  # PALSU

# isalpha(): Memeriksa apakah semua karakter berupa huruf

challenge = 'thirty days of python'
print(challenge.isalpha())  # BENAR
num = '123'
print(num.isalpha())  # PALSU

# isdecimal(): Memeriksa Karakter Desimal

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0

# isdigit(): Memeriksa Karakter Digit

challenge = 'Thirty'
print(challenge.isdigit())  # PALSU
challenge = '30'
print(challenge.isdigit())  # BENAR

# isdecimal():Memeriksa karakter desimal

num = '10'
print(num.isdecimal())  # BENAR
num = '10.5'
print(num.isdecimal())  # PALSU


# isidentifier():Memeriksa pengidentifikasi yang valid berarti memeriksa apakah suatu string adalah nama variabel yang valid

challenge = '30DaysOfPython'
print(challenge.isidentifier())  # Salah, karena dimulai dengan angka
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())  # BENAR


# islower():Memeriksa apakah semua huruf dalam string adalah huruf kecil

challenge = 'thirty days of python'
print(challenge.islower())  # BENAR
challenge = 'Thirty days of python'
print(challenge.islower())  # PALSU

# isupper(): kembali jika semua karakter adalah karakter huruf besar

challenge = 'thirty days of python'
print(challenge.isupper())  # PALSU
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())  # BENAR


# isnumeric():Memeriksa karakter numerik

num = '10'
print(num.isnumeric())  # BENAR
print('ten'.isnumeric())  # PALSU

# join(): Mengembalikan string gabungan

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '  # , '.join(web_tech)
print(result)  # 'HTML# CSS# JavaScript# Bereaksi'

# strip(): Menghapus karakter awal dan akhir

challenge = ' thirty days of python '
print(challenge.strip('y'))  # 5

# replace(): Menggantikan substring di dalamnya

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))  # 'tiga puluh hari pengkodean'

# split():Memisahkan String dari Kiri

challenge = 'thirty days of python'
print(challenge.split())  # ['tiga puluh', 'hari', 'dari', 'python']

# title(): Mengembalikan String Berselubung Judul

challenge = 'thirty days of python'
print(challenge.title())  # Tiga Puluh Hari Python

# swapcase(): Memeriksa apakah String Dimulai dengan String yang Ditentukan

challenge = 'thirty days of python'
print(challenge.swapcase())  # TIGA PULUH HARI PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # TIGA PULUH HARI PYTHON

# dimulai dengan(): Memeriksa apakah String Dimulai dengan String yang Ditentukan

challenge = 'thirty days of python'
print(challenge.startswith('thirty'))  # BENAR
challenge = '30 days of python'
print(challenge.startswith('thirty'))  # PALSU