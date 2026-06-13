try:
    print(10 + '5')
except:
    print('Something went wrong')



try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print("Hasil:", hasil)

except ValueError:
    print("Input harus angka.")

except ZeroDivisionError:
    print("Tidak boleh membagi dengan 0.")


try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2026 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')




try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')




try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else: #dijalankan bila try berhasil 
    print('I usually run with the try block')
finally:#dijalankan selalu mau itu try berhasi/ eror
    print('I alway run.')



#### Membongkar Daftar
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst))


numbers = range(2, 7)  # panggilan normal dengan argumen terpisah
print(list(numbers))  # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # panggilan dengan argumen yang dibongkar dari daftar
print(numbers)  # [2, 3, 4, 5,6]


# numbers = range(2, 7)  # panggilan normal dengan argumen terpisah
# print(list(numbers))  # [2, 3, 4, 5, 6]
# args = [2, 7]
# numbers = range(*args)  # panggilan dengan argumen yang dibongkar dari daftar
# print(numbers)  # [2, 3, 4, 5,6]


countries = ['JKT', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)  # JKTia Swedia Norwegia ['Denmark', 'Islandia']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)  # 1 [2, 3, 4, 5, 6] 7


def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Vincen', 'country':'JKT', 'city':'JAKTIM', 'age':250}
print(unpacking_person_info(**dct))  # Vincen tinggal di JKTia, JAKTIM.Dia berumur 250 tahun.


def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7))


def packing_person_info(**kwargs):
# periksa jenis kwarg dan itu adalah tipe dict
# cetak(ketik(kwargs))
# Mencetak item kamus
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="rz",
      country="JKT", city="JAKTIM", age=250))


# Seperti di JavaScript, penyebaran dapat dilakukan dengan Python.Mari kita periksa pada contoh di bawah ini:

# ```python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['JKT', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['JKTia', 'Swedia', 'Norwegia', 'Denmark', 'Islandia']


for index, item in enumerate([20, 30, 40]):
    print(index, item)
# ```
for nomor, tempat in enumerate(["jakarta", 'bandung', 'jogja']):
    print(nomor+1, tempat)


# ```python
countries = ['JKT', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'JKT':
        print(f'The country {i} has been found at index {index}')



# Terkadang kami ingin menggabungkan daftar saat mengulanginya.Lihat contoh di bawah ini:

# ```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges) 