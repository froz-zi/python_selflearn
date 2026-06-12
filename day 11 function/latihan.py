# 1. Deklarasikan suatu fungsi _add_two_numbers_.Dibutuhkan dua parameter dan mengembalikan jumlah.

def add_two_number (x,y):
    tambah = x + y
    print(tambah) 
    return tambah
add_two_number(2,3)







# 2. Luas lingkaran dihitung sebagai berikut: luas = π x r x r.Tulis fungsi yang menghitung _area_of_circle_.

def hitung_lingkaran(r):
    phi = 3.14
    luas = phi *r*r
    print(f"luas lingkaran dengan jari2 {r} adalah {luas}")
    return luas

hitung_lingkaran(10)



# 3. Tulis fungsi bernama add_all_nums yang mengambil sejumlah argumen dan menjumlahkan semua argumen.Periksa apakah semua item daftar adalah tipe angka.Jika tidak, berikan umpan balik yang masuk akal.
def add_nums (*num):
    total = 0

    for nums in num :
        if type(nums) == int or type(nums) == float :
            total += nums
        else: 
            print(" bukan angka tapi huruf" 
            "")
    return total

print(add_nums(20,20, 10 ))


# 4. Suhu dalam °C dapat diubah ke °F menggunakan rumus berikut: °F = °C x 9/5 + 32. Tuliskan fungsi yang mengubah °C ke °F, _convert_celsius_to-fahrenheit_.
def celsius_to_fahrenheit(x):
    f = x *9/5 + 32

    print("Hasil convert dari celius ke farhenheit adalah : " , f)
    return f

celsius_to_fahrenheit(20)


    
    

# 5. Tulis fungsi bernama check-season, yang mengambil parameter bulan dan mengembalikan musim: Musim Gugur, Musim Dingin, Musim Semi, atau Musim Panas.
# Musim Semi: Maret – MeiMusim Panas: Juni – AgustusMusim Gugur: September – NovemberMusim Dingin: Desember – Februar

def check_season(bulan):
    musim = {
        "Musim Semi": ["Maret", "April", "Mei"],
        "Musim Panas": ["Juni", "Juli", "Agustus"],
        "Musim Gugur": ["September", "Oktober", "November"],
        "Musim Dingin": ["Desember", "Januari", "Februari"]
    }

    for nama_musim, daftar_bulan in musim.items():
        if bulan in daftar_bulan:
            return nama_musim

    return "Bulan tidak valid"


print(check_season("Maret"))
print(check_season("Juli"))
print(check_season("Desember"))
    



# 6. Tulis fungsi bernama hitung_kemiringan yang mengembalikan kemiringan persamaan linier
def hitung_kemiringan(x1, y1, x2, y2):
    kemiringan = (y2 - y1) / (x2 - x1)
    return kemiringan


print(hitung_kemiringan(2, 2, 6, 10))

# 7. Persamaan kuadrat dihitung sebagai berikut: ax² + bx + c = 0. Tuliskan fungsi yang menghitung himpunan solusi persamaan kuadrat, _solve_quadratic_eqn_.

def persamaan_kuadrat(a , b, c , x ):
    hitung_persamaan = a*x*x + b *x + c
    print(hitung_persamaan)
    return hitung_persamaan

persamaan_kuadrat(2,3,4,2)
# 8. Deklarasikan fungsi bernama print_list.Dibutuhkan daftar sebagai parameter dan mencetak setiap elemen daftar.

def print_list(data):
    for item in data:
        print(item)


buah = ["apel", "mangga", "jeruk"]

print_list(buah)

# 9. Deklarasikan fungsi bernama reverse_list.Dibutuhkan array sebagai parameter dan mengembalikan kebalikan dari loop penggunaan array.
def reverse_list (*args):
    data_reverse = list(reversed(args))
    print(data_reverse)
    return data_reverse

reverse_list(1,2,3,4,5)

#10. Deklarasikan fungsi bernama capitalize_list_items.Dibutuhkan daftar sebagai parameter dan mengembalikan daftar item dengan huruf kapital

def capitalize_list_items(*args):
    data_capitalize =  []

    for item in args :
        data_capitalize.append(item.upper())

    return data_capitalize

print(capitalize_list_items("indonesia" , "malay"))

#11. Deklarasikan fungsi bernama add_item.Dibutuhkan daftar dan parameter item.Ini mengembalikan daftar dengan item yang ditambahkan di akhir.

def add_item (food_stuff, item):
    food_stuff.append(item)
    return food_stuff


food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']

add_item(food_stuff, 'wortel')
print(food_stuff)

# 12. Deklarasikan fungsi bernama hapus_item.Dibutuhkan daftar dan parameter item.Ini mengembalikan daftar dengan item yang dihapus darinya.    

def del_item (food, item2):
    food.remove(item2)
    return food

food = ['Potato', 'Tomato', 'Mango', 'Milk']

del_item(food,'Potato')
print(food)

# 13. Deklarasikan fungsi bernama sum_of_numbers.Dibutuhkan parameter angka dan menambahkan semua angka dalam rentang itu.

def sum_of_numbers(y):
    total = 0

    for x in range (y+1) :
        total += x
    
    return total


print(sum_of_numbers(5))

# 14. Deklarasikan fungsi bernama sum_of_odds.Dibutuhkan parameter angka dan menambahkan semua angka ganjil dalam rentang tersebut.

def sum_odd(y):
    data = 0 

    for x in range(y + 1):
        if x % 2 != 0:
            data += x
    return data


print(sum_odd (100))

# 15. Deklarasikan fungsi bernama sum_of_even.Dibutuhkan parameter angka dan menambahkan semua angka genap dalam rentang tersebut.

def sum_even(y):
    data = 0 

    for x in range(y + 1):
        if x % 2 == 0:
            data += x
    return data


print(sum_even (100))

# 1. Deklarasikan fungsi bernama evens_and_odds .Dibutuhkan bilangan bulat positif sebagai parameter dan menghitung jumlah genap dan ganjil dalam nomor tersebut.

def evens_and_odds(y):
    jumlah_genap = 0
    jumlah_ganjil = 0

    for x in range(y + 1):
        if x % 2 == 0:
            jumlah_genap += 1
        else:
            jumlah_ganjil += 1

    return f"oddsnya  {jumlah_ganjil}\nevensnya  {jumlah_genap}"


print(evens_and_odds(100))

# 1. Panggil fungsi Anda faktorial, dibutuhkan bilangan bulat sebagai parameter dan mengembalikan faktorial dari bilangan tersebut

def factorial(z):
    total = 1

    for x in range(1, z + 1):
        total = total * x
    return total

print(factorial(5))  

# 1. Panggil fungsi Anda _is_empty_, dibutuhkan parameter dan memeriksa apakah kosong atau tidak


def is_empty (data):
    if len(data) == 0:
        return " data kosong"
    else: return " data tak kosong"

print(is_empty([]))
print(is_empty([1, 2, 3]))
print(is_empty(""))
print(is_empty("Fahrul"))

#1. Tulis berbagai fungsi yang mengambil daftar.Mereka harus menghitung_mean, menghitung_median, 
# menghitung_mode, menghitung_range, menghitung_variance, menghitung_std standar deviasi.

def calculate_mean(data):
    total = sum(data)
    banyak_data = len(data)
    mean = total / banyak_data
    return mean


def calculate_median(data):
    data_urut = sorted(data)
    n = len(data_urut)

    if n % 2 == 1:
        tengah = n // 2
        return data_urut[tengah]
    else:
        tengah1 = data_urut[n // 2 - 1]
        tengah2 = data_urut[n // 2]
        return (tengah1 + tengah2) / 2


def calculate_mode(data):
    frekuensi = {}

    for angka in data:
        if angka in frekuensi:
            frekuensi[angka] += 1
        else:
            frekuensi[angka] = 1

    mode = max(frekuensi, key=frekuensi.get)
    return mode


def calculate_range(data):
    return max(data) - min(data)


def calculate_variance(data):
    mean = calculate_mean(data)
    total = 0

    for angka in data:
        total += (angka - mean) ** 2

    variance = total / len(data)
    return variance


def calculate_std(data):
    variance = calculate_variance(data)
    std = variance ** 0.5
    return std


data = [1, 2, 2, 3, 4, 5, 5, 5, 6]

print("Mean:", calculate_mean(data))
print("Median:", calculate_median(data))
print("Mode:", calculate_mode(data))
print("Range:", calculate_range(data))
print("Variance:", calculate_variance(data))
print("Standard Deviation:", calculate_std(data)) #pake ai kalo ini





