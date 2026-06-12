
daftar = []
daftar = ['pisang','jeruk', 'apel', 'kiwi', 'anggur']
print('Banyak buah',len(daftar))


tipe_data_campuran = ['Fahrul', 23, 170, 'belum', 'bandung']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(tipe_data_campuran)
print('jumlah perusahaan ', len(it_companies))
last_index = len(it_companies) - 1
last_perusahaan = it_companies[last_index]
print(last_perusahaan)

print(it_companies[0], it_companies[3],last_perusahaan)
it_companies.append('Discord')

print(it_companies)
last_index = len(it_companies) - 1
last_perusahaan = it_companies[last_index]
print(last_perusahaan)

it_companies.insert(3, 'GitHub')
print(it_companies)

index_github = it_companies.index('GitHub')
it_companies[index_github] = it_companies[index_github].upper()

print(it_companies)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'GitHub']

hasil = '#; '.join(it_companies)

print(hasil)

adakah_disana = 'Facebook'in it_companies
print(adakah_disana)

it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)

perusahaan_3_pertama = it_companies[0 : 3]
print(perusahaan_3_pertama)

perusahaan_3_terakhir = it_companies[-4 : -1]
print(perusahaan_3_terakhir)

perusahaan_tengah = it_companies[4]
print(perusahaan_tengah)

del it_companies[0]
print(it_companies)

del it_companies[3]
print(it_companies)

del it_companies[-1]
print(it_companies)

it_companies.clear()
print(it_companies)


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

index_frontend = front_end.index('Redux')
front_end.insert(index_frontend  + 1 , 'SQL')

print(front_end)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
nilai_max = max(ages)
nilai_min = min(ages)

print(nilai_max)
print(nilai_min)
ages.extend([18, 25])
ages.sort()
print(ages)

#mencari median 
import statistics

median_ages = statistics.median(ages)
print(median_ages)
mean_ages = statistics.mean(ages)
print(mean_ages)
rentang_usia = nilai_max - nilai_min
print(rentang_usia)


average = statistics.mean(ages)
selisih_min = abs(nilai_min - average)
selisih_max = abs(nilai_max - average)
print(f"Average: {average}")
print(f"Min: {nilai_min}, Selisih dari average: {selisih_min}")
print(f"Max: {nilai_max}, Selisih dari average: {selisih_max}")

# Bandingkan
if selisih_min > selisih_max:
    print(f"✓ Min lebih jauh dari average")
elif selisih_max > selisih_min:
    print(f"✓ Max lebih jauh dari average")
else:
    print(f"✓ Min dan Max sama jauhnya dari average")