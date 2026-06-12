## Ekspresi Reguler

# Ekspresi reguler atau RegEx adalah string teks khusus yang membantu menemukan pola dalam data.RegEx dapat digunakan untuk memeriksa apakah ada pola tertentu dalam tipe data yang berbeda.Untuk menggunakan RegEx dengan python terlebih dahulu kita harus mengimpor modul RegEx yang disebut *re*.

### Modul *re*

# Setelah mengimpor modul kita dapat menggunakannya untuk mendeteksi atau menemukan pola.


# sintaksis
# re.match(substring, string, re.I)

import re
txt = 'I love to teach python and javaScript'
match = re.match('I love to teach', txt, re.I) #re.I = ignore case, artinya tidak membedakan huruf besar dan huruf kecil.
print(match)

import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# Ia mengembalikan objek dengan rentang dan kecocokan
match = re.search('first', txt, re.I)
print(match)  # <re.Cocokkan objek;span=(100, 105), cocok='pertama'>
# Kita bisa mendapatkan posisi awal dan akhir pertandingan sebagai tupel menggunakan span
span = match.span()
print(span)  # (100, 105)
# Mari kita cari posisi awal dan akhir dari rentang tersebut
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)  # Pertama


txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# Ini mengembalikan daftar
matches = re.findall('language', txt, re.I)
print(matches)  # ['bahasa', 'bahasa']



txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# Ini mengembalikan daftar
matches = re.findall('language', txt, re.I)
print(matches)  # ['bahasa', 'bahasa']



txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# Ini mengembalikan daftar
import re

txt = "I love this language. LANGUAGE is important."

matches = re.findall("language", txt, re.I)

print(matches)

import re


txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Piton', 'Piton']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Piton', 'Piton']


#### Mengganti Substring

import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript adalah bahasa terindah yang pernah dibuat manusia. Saya merekomendasikan python untuk bahasa pemrograman pertama
# ATAU
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript adalah bahasa terindah yang pernah dibuat manusia. Saya merekomendasikan python untuk bahasa pemrograman pertama


import re
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt))  # pemisahan menggunakan \n - simbol akhir garis

import re

text = "apel,jeruk;mangga pisang"

hasil = re.split(r"[,; ]", text)

print(hasil)



import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apel']\


import re
regex_pattern = r'[a]..'  # tanda kurung siku ini artinya a dan .berarti karakter apa pun kecuali baris baru
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'[a].*'  # .karakter apa pun, * karakter apa pun nol kali atau lebih
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)


### Nol atau satu kali?

# Nol atau satu kali.Polanya mungkin tidak muncul atau mungkin terjadi satu kali saja.

# ```python
import re
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ?berarti di sini bahwa '-' adalah opsional
matches = re.findall(regex_pattern, txt)
print(matches)


### Penghitung di RegEx

# Kita dapat menentukan panjang substring yang kita cari dalam sebuah teks, menggunakan tanda kurung kurawal.Bayangkan, kita tertarik pada substring dengan panjang 4 karakter:

# ```python

import re
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # tepat empat kali
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1,4}'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']



import re
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ artinya dimulai dengan
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']


# - Negasi


txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ dalam himpunan karakter berarti negasi, bukan A sampai Z, bukan a sampai z, tanpa spasi
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']