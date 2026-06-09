# is di Python dipakai untuk mengecek apakah dua variabel menunjuk ke objek yang sama di memori.
#Sedangkan == dipakai untuk mengecek apakah nilainya sama.


a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

print("="*10)
a = [1, 2, 3]
b = a

print(a == b)
print(a is b)

print("="*10)


# data = None

# if data is None:
#     print("Data kosong")
# else:
#     print("Data ada")

data = None

if data is None:
    print ("ASD")
else: print("asasdasasd")