# 1. Kata apa yang paling sering muncul pada paragraf berikut?



paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

import re
from collections import Counter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r'\b\w+\b', paragraph)

word_count = Counter(words)

result = [(count, word) for word, count in word_count.items()]

result.sort(reverse=True)

print(result)#ai


# 2. Letak beberapa partikel pada sumbu x mendatar adalah -12, -4, -3 dan -1 pada arah negatif, 0 pada titik asal, 4 dan 8 pada arah positif.Ekstrak angka-angka ini dari keseluruhan teks ini dan temukan jarak antara dua partikel terjauh.

points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12)  # 20


text = "Letak beberapa partikel pada sumbu x mendatar adalah -12, -4, -3 dan -1 pada arah negatif, 0 pada titik asal, 4 dan 8 pada arah positif."

points = re.findall(r'-?\d+', text)

print(points)

points = [int(point) for point in points]

distance = max(points) - min(points)

print(points)
print(distance)



# 1. Tulis pola yang mengidentifikasi apakah suatu string adalah variabel python yang valid

#     ```sh
#     is_valid_variable('first_name') # True
#     is_valid_variable('first-name') # False
#     is_valid_variable('1first_name') # False
#     is_valid_variable('firstname') # True

import re

def is_valid_variable(name):
    pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
    return bool(re.fullmatch(pattern, name))


print(is_valid_variable('first_name'))   # True
print(is_valid_variable('first-name'))   # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))    # Truez
# 1. Bersihkan teks berikut.Setelah dibersihkan, hitung tiga kata yang paling sering muncul dalam string.

#     ```python
#     sentence = '''%I $am@% a %tea@cher%, &and& I lo%  # dan %teh@ching%;.Tidak ada apa-apa;&as& mo@re bermanfaat sebagai educa@ting &and& @emp%o@wering peo@ple.;Menurutku tea@ching m%o@re menarik dibandingkan %jo@bs lainnya.%Apakah@es ini%s mo@tivate yo@u menjadi tea@cher!?'''

#     print(clean_text(sentence));
#     I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
#     print(most_frequent_words(cleaned_text))  # [(3, 'Saya'), (2, 'mengajar'), (2, 'guru')]

import re

sentence = '''%I $am@% a %tea@cher%, &and& I lo%ve %teh@ching%;.Tidak ada apa-apa;&as& mo@re bermanfaat sebagai educa@ting &and& @emp%o@wering peo@ple.;Menurutku tea@ching m%o@re menarik dibandingkan %jo@bs lainnya.%Apakah@es ini%s mo@tivate yo@u menjadi tea@cher!?'''

def clean_text(text):
    cleaned_text = re.sub(r'[%$@&;,.!?]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    return cleaned_text.strip()


def most_frequent_words(text):
    words = re.findall(r'\b\w+\b', text)

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    result = []

    for word, count in word_count.items():
        result.append((count, word))

    result.sort(reverse=True)

    return result[:3]


cleaned_text = clean_text(sentence)

print(cleaned_text)
print(most_frequent_words(cleaned_text))