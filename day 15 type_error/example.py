# ## Jenis Kesalahan Python

# Saat kita menulis kode, sering kali kita salah ketik atau kesalahan umum lainnya.Jika kode kita gagal dijalankan, juru bahasa Python akan menampilkan pesan, berisi umpan balik dengan informasi tentang lokasi terjadinya masalah dan jenis kesalahannya.Terkadang juga memberi kami saran tentang kemungkinan perbaikan.Memahami berbagai jenis kesalahan dalam bahasa pemrograman akan membantu kita men-debug kode dengan cepat dan juga membuat kita lebih baik dalam melakukan apa yang kita lakukan.

# Mari kita lihat jenis kesalahan yang paling umum satu per satu.Pertama mari kita buka shell interaktif Python kita.Buka terminal komputer Anda dan tulis 'python'.Shell interaktif python akan dibuka.

# ### Kesalahan Sintaks

# **Contoh 1: SintaksError**

# ```python
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print 'hello world'
#   File "<stdin>", line 1
#     print 'hello world'
#                       ^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
# >>>
# ```

# Seperti yang Anda lihat, kami membuat kesalahan sintaksis karena kami lupa menyertakan string dengan tanda kurung dan Python sudah menyarankan solusinya.Mari kita memperbaikinya.

# ```python
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print 'hello world'
#   File "<stdin>", line 1
#     print 'hello world'
#                       ^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
# >>> print('hello world')
# hello world
# >>>
# ```

# Kesalahannya adalah _SyntaxError_.Setelah perbaikan, kode kami dijalankan tanpa hambatan.Mari kita lihat lebih banyak jenis kesalahan.

# ### Kesalahan Nama

# **Contoh 1: Kesalahan Nama**

# ```python
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print(age)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'age' is not defined
# >>>
# ```

# Seperti yang Anda lihat dari pesan di atas, nama umur tidak ditentukan.Ya, benar bahwa kami tidak mendefinisikan variabel usia tetapi kami mencoba mencetaknya seolah-olah kami telah mendeklarasikannya.Sekarang, mari kita perbaiki dengan mendeklarasikannya dan memberikan nilai.

# ```python
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print(age)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'age' is not defined
# >>> age = 25
# >>> print(age)
# 25
# >>>
# ```

# Jenis kesalahannya adalah _NameError_.Kami men-debug kesalahan dengan mendefinisikan nama variabel.

# ### Kesalahan Indeks

# **Contoh 1: IndexError**

# ```python
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> numbers = [1, 2, 3, 4, 5]
# >>> numbers[5]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>>
# ```

# Pada contoh di atas, Python memunculkan _IndexError_, karena daftarnya hanya memiliki indeks dari 0 hingga 4, sehingga berada di luar jangkauan.

# ### ModuleNotFoundError

# **Contoh 1: ModuleNotFoundError**

# ```python
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import maths
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'maths'
# >>>
# ```

# Dalam contoh di atas, saya sengaja menambahkan s tambahan ke matematika dan _ModuleNotFoundError_ dimunculkan.Mari kita perbaiki dengan menghapus s tambahan dari matematika.

# ```python
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import maths
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'maths'
# >>> import math
# >>>
# ```

# Kami memperbaikinya, jadi mari gunakan beberapa fungsi dari modul matematika.

# ### Kesalahan Atribut

# **Contoh 1: AttributeError**

# ```python
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import maths
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'maths'
# >>> import math
# >>> math.PI
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'math' has no attribute 'PI'
# >>>
# ```

# Seperti yang Anda lihat, saya melakukan kesalahan lagi!Alih-alih pi, saya mencoba memanggil konstanta PI dari modul matematika.Hal ini menimbulkan kesalahan atribut, artinya atribut tersebut tidak ada pada modul.Mari kita perbaiki dengan mengubah dari PI ke pi.

# ```python
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import maths
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'maths'
# >>> import math
# >>> math.PI
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'math' has no attribute 'PI'
# >>> math.pi
# 3.141592653589793
# >>>
# ```

# Sekarang, saat kita memanggil pi dari modul matematika, kita mendapatkan hasilnya.

# ### Kesalahan Kunci

# **Contoh 1: Kesalahan Kunci**

# ```python
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
# >>> users['name']
# 'Asab'
# >>> users['county']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'county'
# >>>
# ```

# Seperti yang Anda lihat, ada kesalahan ketik pada kunci yang digunakan untuk mendapatkan nilai kamus.jadi, ini adalah kesalahan utama dan perbaikannya cukup mudah.Ayo lakukan ini!

# ```python
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> user = {'name':'Asab', 'age':250, 'country':'Finland'}
# >>> user['name']
# 'Asab'
# >>> user['county']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'county'
# >>> user['country']
# 'Finland'
# >>>
# ```

# Kami men-debug kesalahan tersebut, kode kami dijalankan dan kami mendapatkan nilainya.

# ### Kesalahan Ketik

# **Contoh 1: TypeError**

# ```python
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 4 + '3'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >>>
# ```

# Pada contoh di atas, TypeError dimunculkan karena kita tidak dapat menambahkan angka ke dalam string.Solusi pertama adalah mengubah string menjadi int atau float.Solusi lain adalah mengubah angka menjadi string, hasilnya adalah '43'.Mari kita ikuti perbaikan pertama.

# ```python
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 4 + '3'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >>> 4 + int('3')
# 7
# >>> 4 + float('3')
# 7.0
# >>>
# ```

# Kesalahan dihapus dan kami mendapatkan hasil yang kami harapkan.

# ### Kesalahan Impor

# **Contoh 1: TypeError**

# ```python
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from math import power
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: cannot import name 'power' from 'math'
# >>>
# ```

# Tidak ada fungsi yang disebut power dalam modul matematika, ia memiliki nama yang berbeda: _pow_.Mari kita perbaiki:

# ```python
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from math import power
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: cannot import name 'power' from 'math'
# >>> from math import pow
# >>> pow(2,3)
# 8.0
# >>>
# ```

# ### NilaiKesalahan

# ```python
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> int('12a')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '12a'
# >>>
# ```

# Dalam hal ini kita tidak dapat mengubah string yang diberikan menjadi angka, karena ada huruf 'a' di dalamnya.

# ### ZeroDivisionError

# ```python
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 1/0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# >>>
# ```


