## Kamus

# Kamus adalah kumpulan kunci berpasangan yang tidak berurutan dan dapat diubah: tipe data nilai.

# ### Membuat Kamus

# Untuk membuat kamus kami menggunakan tanda kurung kurawal, {} atau fungsi bawaan *dict*.

# sintaksis
empty_dict = {}
# Kamus dengan nilai data
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}


# **Contoh:**


person = {
    'first_name':'Vincen',
    'last_name':'Babi',
    'age':190,
    'country':'Indo',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }


# Kamus di atas menunjukkan bahwa suatu nilai dapat berupa tipe data apa pun: string, boolean, list, tuple, set, atau kamus.

# ### Panjang Kamus

# Ia memeriksa jumlah pasangan 'kunci: nilai' dalam kamus.


# sintaksis
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct))  # 4


# **Contoh:**


person = {
    'first_name':'Vincen',
    'last_name':'Babi',
    'age':190,
    'country':'Indo',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(len(person))  # 7



### Mengakses Item Kamus

# Kita dapat mengakses item Kamus dengan merujuk pada nama kuncinya.


# sintaksis
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1'])  # nilai1
print(dct['key4'])  # nilai4


# **Contoh:**


person = {
    'first_name':'Vincen',
    'last_name':'Babi',
    'age':190,
    'country':'Indo',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['first_name'])  # Asabene
print(person['country'])  # Indoia
print(person['skills'])  # ['JavaScript', 'Reaksi', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street'])  # Jalan luar angkasa
# print(person['city'])  # Kesalahan


# Mengakses item dengan nama kunci menimbulkan kesalahan jika kuncinya tidak ada.Untuk menghindari kesalahan ini terlebih dahulu kita harus memeriksa apakah ada kunci atau kita dapat menggunakan metode _get_.Metode get mengembalikan Tidak Ada, yang merupakan tipe data objek NoneType, jika kuncinya tidak ada.

person = {
    'first_name':'Vincen',
    'last_name':'Babi',
    'age':190,
    'country':'Indo',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person.get('first_name'))  # Asabene
print(person.get('country'))  # Indoia
print(person.get('skills'))  # ['JavaScript', 'Reaksi', 'Node', 'MongoDB', 'Python']
print(person.get('city'))  # Tidak ada


### Menambahkan Item ke Kamus

# Kita dapat menambahkan pasangan kunci dan nilai baru ke kamus


# sintaksis
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'


# **Contoh:**


person = {
    'first_name':'Vincen',
    'last_name':'Babi',
    'age':190,
    'country':'Indo',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)


### Memodifikasi Item dalam Kamus

# Kita dapat memodifikasi item dalam kamus


# sintaksis
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'


# **Contoh:**


person = {
    'first_name':'Vincen',
    'last_name':'Babi',
    'age':190,
    'country':'Indo',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person['first_name'] = 'Eyob'
person['age'] = 252


### Memeriksa Kunci dalam Kamus

# Kami menggunakan operator _in_ untuk memeriksa apakah ada kunci di kamus


# sintaksis
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct)  # BENAR
print('key5' in dct)  # PALSU


### Menghapus Pasangan Kunci dan Nilai dari Kamus

# - _popkey_: menghapus item dengan nama kunci yang ditentukan:
# - _popitem_: menghapus item terakhir
# - _del_: menghapus item dengan nama kunci tertentu


# sintaksis
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1')  # menghapus item kunci1
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem()  # menghapus item terakhir
del dct['key2']  # menghapus item kunci2


# **Contoh:**


person = {
    'first_name':'Vincen',
    'last_name':'Babi',
    'age':190,
    'country':'Indo',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person.pop('first_name')  # Menghapus item nama depan
person.popitem()  # Menghapus item alamat
del person['is_married']  # Menghapus item is_married


### Mengubah Kamus ke Daftar Item

# Metode _items_ mengubah kamus menjadi daftar tupel.


# sintaksis
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())  # dict_items([('kunci1', 'nilai1'), ('kunci2', 'nilai2'), ('kunci3', 'nilai3'), ('kunci4', 'nilai4')])


### Menghapus Kamus

# Jika kita tidak menginginkan item dalam kamus kita dapat menghapusnya menggunakan metode _clear_


# sintaksis
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear())  # Tidak ada


### Menghapus Kamus

# Jika kami tidak menggunakan kamus, kami dapat menghapusnya sepenuhnya


# sintaksis
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct


### Salin Kamus

# Kita dapat menyalin kamus menggunakan metode _copy_.Dengan menggunakan salinan kita dapat menghindari mutasi kamus asli.


# sintaksis
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()  # {'kunci1':'nilai1', 'kunci2':'nilai2', 'kunci3':'nilai3', 'kunci4':'nilai4'}


### Mendapatkan Kunci Kamus sebagai Daftar

# Metode _keys_ memberi kita semua kunci kamus sebagai daftar.


# sintaksis
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)  # dict_keys(['kunci1', 'kunci2', 'kunci3', 'kunci4'])


### Mendapatkan Nilai Kamus sebagai Daftar

# Metode _values_ memberi kita semua nilai kamus sebagai daftar.

# sintaksis
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)  # dict_values(['nilai1', 'nilai2', 'nilai3', 'nilai4'])
