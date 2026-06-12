# 1. Dapatkan masukan pengguna menggunakan masukan “Masukkan usia Anda: ”.
# Jika pengguna berusia 18 tahun ke atas, berikan masukan: Anda cukup 
# umur untuk mengemudi.Jika dibawah 18 berikan feedback untuk menunggu jumlah tahun yang hilang.Keluaran:

umur = int(input("masukan umur anda: "))
kurang_umur = 18 - umur
if umur < 18:
    print(f"umur anda kurang {kurang_umur}")
elif umur >= 18:
    print("anda sudah bisa berkemudi")


# 2. Bandingkan nilai my_age dan your_age menggunakan if… else.Siapa yang lebih tua dari saya 
# atau Anda?Gunakan input “Masukkan umur Anda: ” untuk mendapatkan umur sebagai masukan.Anda dapat menggunakan 
# kondisi bersarang untuk mencetak 'tahun' untuk perbedaan usia 
# 1 tahun, 'tahun' untuk perbedaan yang lebih besar, dan teks khusus jika usia_saya = usia_Anda.Keluaran:

umur_saya = 20 
umur_anda = int(input("Masukan umur anda"))
perbandingan = abs(umur_saya - umur_anda)

if umur_anda > umur_saya or umur_anda < umur_saya:
    print(f"umur kita berbeda {perbandingan}")
elif umur_anda == umur_saya :
    print("kita seumuran")

# 3. Dapatkan dua nomor dari pengguna menggunakan input prompt.
# Jika a lebih besar dari b maka hasil a lebih besar dari b, 
# jika a lebih kecil dari b maka hasil a lebih kecil dari b, jika tidak a sama dengan b.Keluaran:


a = int(input(" nomor a : "))
b = int(input(" nomor b : "))

if a > b :
    print ("a lebih besar")
else: print(" b lebih besar ")

# 1. Tuliskan kode yang memberikan nilai kepada siswa berdasarkan nilai mereka:

#     ```sh
#     90-100, A
#     80-89, B
#     70-79, C
#     60-69, D
#     0-59, F
#     ```

nilai = int(input("Masukan nilai anda"))
if nilai >= 90  and nilai <= 100:
    print("Nilai anda A")
elif nilai >= 80 and nilai <90 :
    print("Nilai anda B ")
elif nilai >= 70 and nilai < 80:
    print("nilai anda C")
elif nilai >= 60 and nilai < 70:
    print("nilai anda D")
else : print (" anda tidak lulus ")

# * Periksa apakah kamus orang tersebut memiliki kunci keterampilan, jika ada, cetaklah keterampilan tengah dalam daftar keterampilan.
# * Periksa apakah kamus orang tersebut memiliki kunci keterampilan, jika demikian periksa apakah orang tersebut 
# memiliki keterampilan 'Python' dan cetak hasilnya.
# * Jika keterampilan seseorang hanya memiliki JavaScript dan React, cetak 'Dia adalah pengembang front end', 
# jika keterampilan orang tersebut memiliki Node, Python, MongoDB, cetak 'Dia adalah pengembang backend', 
# jika keterampilan orang tersebut memiliki React, Node dan MongoDB, Cetak 'Dia adalah pengembang fullstack', 
# jika tidak, cetak 'judul tidak dikenal' - untuk hasil yang lebih akurat, lebih banyak kondisi dapat disarangkan!
# * Jika orang tersebut sudah menikah dan tinggal di indo.

person={
    'first_name': 'rozi',
    'last_name': 'zi',
    'age': 25,
    'country': 'indo',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if person["skills"] == ["python"] :
    print(" anda memiliki skill python")
elif person["skills"] == ["Javascript", "React", "MongoDB"] :
    print(" anda pengembang backend")
elif person["skills"] == ["Node", "React", "MongoDB"]:
    print("Anda fullstack dev ")
elif person["is_married"] == True and person["country"] == "indo":
    print (f"{person['first_name']} tinggal di  {person["country"]} dan sudah menikah " )