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