## Set

# Set adalah kumpulan item.Izinkan saya membawa Anda kembali ke pelajaran Matematika sekolah dasar atau menengah Anda.Definisi Matematika dari suatu himpunan juga dapat diterapkan dengan Python.Set adalah kumpulan elemen berbeda yang tidak berurutan dan tidak diindeks.Dalam Python set digunakan untuk menyimpan item unik, dan dimungkinkan untuk menemukan _union_, _intersection_, _difference_, _symmetric Difference_, _subset_, _super set_ dan _disjoint set_ di antara set.



st = set()

### Memeriksa Barang
st = {'item1', 'item2', 'item3', 'item4'}
fruits = {'banana', 'orange', 'mango', 'lemon'}
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
len(fruits)


st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st)
print('mango' in fruits )

# sintaksis add
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')


# - Tambahkan beberapa item menggunakan _update_
# _update_ memungkinkan untuk menambahkan beberapa item ke satu set._update_ mengambil argumen daftar.
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])

### Menghapus Item dari Set
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')