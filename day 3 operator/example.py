# Operasi Aritmatika dengan Python
# bilangan bulat

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
# Pembagian dengan python memberikan angka mengambang
print('Division: ', 4 / 2)
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
# memberi tanpa angka mengambang atau tanpa sisa
print('Division without the remainder: ', 7 // 2)
print('Modulus: ', 3 % 2)  # Memberikan sisanya
print('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)  # artinya 3*3

# Angka mengambang
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Bilangan kompleks
print('Complex number: ', 1+1j)
print('Multiplying complex number: ', (1+1j) * (1-1j))

# Mendeklarasikan variabel paling atas terlebih dahulu

a = 3  # a adalah nama variabel dan 3 adalah tipe data integer
b = 2  # b adalah nama variabel dan 3 adalah tipe data integer

# Operasi aritmatika dan menugaskan hasilnya ke variabel
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# Saya seharusnya menggunakan jumlah alih-alih total tetapi jumlah adalah fungsi bawaan, cobalah untuk menghindari mengesampingkan fungsi bawaan
print(total)  # jika Anda tidak memberi label pada cetakan Anda dengan suatu string, Anda tidak akan pernah tahu dari mana hasilnya
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Mendeklarasikan nilai-nilai dan mengaturnya bersama-sama
num_one = 3
num_two = 4

# Operasi aritmatika
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Mencetak nilai dengan label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Menghitung luas lingkaran
radius = 10  # radius lingkaran
# tanda dua * berarti eksponen atau pangkat
area_of_circle = 3.14 * radius ** 2
print('Area of a circle:', area_of_circle)

# Menghitung luas persegi panjang
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Menghitung berat suatu benda
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)  # Benar, karena 3 lebih besar dari 2
print(3 >= 2)  # Benar, karena 3 lebih besar dari 2
print(3 < 2)  # Salah, karena 3 lebih besar dari 2
print(2 < 3)  # Benar karena 2 lebih kecil dari 3
print(2 <= 3)  # Benar karena 2 lebih kecil dari 3
print(3 == 2)  # Salah, karena 3 tidak sama dengan 2
print(3 != 2)  # Benar, karena 3 tidak sama dengan 2
print(len('mango') == len('avocado'))  # PALSU
print(len('mango') != len('avocado'))  # BENAR
print(len('mango') < len('avocado'))  # BENAR
print(len('milk') != len('meat'))  # PALSU
print(len('milk') == len('meat'))  # BENAR
print(len('tomato') == len('potato'))  # BENAR
print(len('python') > len('dragon'))  # PALSU

# Perbandingan Boolean
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Perbandingan cara lain
# Benar - karena nilai datanya sama
print('1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)  # Benar - karena 1 bukan 2
print('A in Asabeneh', 'A' in 'Asabeneh')  # Benar - A ditemukan di string
print('B in Asabeneh', 'B' in 'Asabeneh')  # Salah -tidak ada huruf besar B
# Benar - karena coding untuk semua memiliki kata coding
print('coding' in 'coding for all')
print('a in an:', 'a' in 'an')  # BENAR
print('4 is 2 ** 2:', 4 is 2 ** 2)  # BENAR

print(3 > 2 and 4 > 3)  # Benar - karena kedua pernyataan itu benar
print(3 > 2 and 4 < 3)  # Salah - karena pernyataan kedua salah
print(3 < 2 and 4 < 3)  # Salah - karena kedua pernyataan tersebut salah
print(3 > 2 or 4 > 3)  # Benar - karena kedua pernyataan itu benar
print(3 > 2 or 4 < 3)  # Benar - karena salah satu pernyataannya benar
print(3 < 2 or 4 < 3)  # Salah - karena kedua pernyataan tersebut salah
print(not 3 > 2)  # Salah - karena 3 > 2 benar, maka tidak Benar menghasilkan Salah
print(not True)  # Salah - Negasi, operator bukan mengubah benar menjadi salah
print(not False)  # BENAR
print(not not True)  # BENAR
print(not not False)  # PALSU   