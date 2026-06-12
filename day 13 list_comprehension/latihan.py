# 1. Filter hanya negatif dan nol dalam daftar menggunakan pemahaman daftar
#    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negatif = [x for x in numbers if x <= 0 ]
print(negatif)

# 2. Ratakan daftar list berikut menjadi list satu dimensi :

#    ```python
#    list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#    output
#    [1, 2, 3, 4, 5, 6, 7, 8, 9]


list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
urutan = [data_panjang for data_list in list_of_lists for data_panjang in data_list]
print(urutan)

# 3. Dengan menggunakan pemahaman list, buatlah daftar tupel berikut:
#    ```python
#    [(0, 1, 0, 0, 0, 0, 0),
#    (1, 1, 1, 1, 1, 1, 1),
#    (2, 1, 2, 4, 8, 16, 32),
#    (3, 1, 3, 9, 27, 81, 243),
#    (4, 1, 4, 16, 64, 256, 1024),
#    (5, 1, 5, 25, 125, 625, 3125),
#    (6, 1, 6, 36, 216, 1296, 7776),
#    (7, 1, 7, 49, 343, 2401, 16807),
#    (8, 1, 8, 64, 512, 4096, 32768),
#    (9, 1, 9, 81, 729, 6561, 59049),
#    (10, 1, 10, 100, 1000, 10000, 100000)]

numbers = [(i, i**0, i**1 , i**2 , i**3, i**4 , i**5) for i in range(11)]
print(numbers)


# 4. Ratakan daftar berikut ke daftar baru:
#    ```python
#    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#    output:
#    [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

rata_negara = [ 
    [country.upper(), country[:3].upper(), capital.upper()]
    for row in countries
    for country , capital  in row 
]

print(rata_negara)


# 5. Ubah daftar berikut menjadi daftar kamus:
#    ```python
#    
#    output:
#    [{'country': 'FINLAND', 'city': 'HELSINKI'},
#    {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#    {'country': 'NORWAY', 'city': 'OSLO'}]


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

negara =  [ {'country': country.upper() , 'city': city.upper()  }
           
           for data in countries
           for country , city in data

]
print(negara)

# 6. Ubah daftar daftar berikut menjadi daftar string gabungan:
#    ```python

# names = [[('Adam', 'Smith')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
#    ['Adam Smith', 'David Smith', 'Donald Trump', 'Bill Gates']
names = [[('Adam', 'Smith')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

gabungan = [ nama_depan +' '+ nama_belakang
            for x in names
            for nama_depan , nama_belakang in x
            ]

print(gabungan)

#7. Tulislah fungsi lambda yang dapat menyelesaikan kemiringan atau perpotongan y dari fungsi linier.

kemiringan = lambda m,x,b : (m*x)+b
print (kemiringan(2,5,1))