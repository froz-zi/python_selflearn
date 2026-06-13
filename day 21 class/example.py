# Creating a Class

# syntax
# class ClassName:
#   code goes here

class person:
 def __init__(self, namadepan, namabelakang, umur, negara, kota):
  self.firstname = namadepan
  self.lastname = namabelakang
  self.age = umur
  self.country = negara
  self.city = kota



data_orang = person('Fahrul','Rozi','23', 'Indonesia', 'Bogor')
print(data_orang.firstname)
print(data_orang.lastname)
print(data_orang.age)
print(data_orang.country)
print(data_orang.city)

# atau menggunakan fungsi sbg object
class person:
    def __init__(self, namadepan = 'fahrul', namabelakang = 'rozi', umur = ' 22', negara= ' indo', kota= 'bogor'):
         self.firstname = namadepan
         self.lastname = namabelakang
         self.age = umur
         self.country = negara
         self.city = kota
    def data_orang (self):
        return f'{self.firstname}{self.lastname} is {self.age} years old . He lived on {self.country}, {self.city}'

p1 = person()
print(p1.data_orang())
p2 = person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.data_orang())



class person:
    def __init__(self, namadepan = 'fahrul', namabelakang = 'rozi', umur = ' 22', negara= ' indo', kota= 'bogor'):
         self.firstname = namadepan
         self.lastname = namabelakang
         self.age = umur
         self.country = negara
         self.city = kota
         self.skills = []
    def data_orang (self):
        return f'{self.firstname}{self.lastname} is {self.age} years old . He lived on {self.country}, {self.city}'
    def add_skill(self, skill):
        self.skills.append(skill)

print("output")
p1 = person()
print(p1.data_orang())

p1.add_skill("HTML")
p1.add_skill("CSS")
print(p1.skills)
print(p1.data_orang())


# Inheritance
# Dengan menggunakan Inheritance, kita dapat menggunakan kembali kode kelas induk. Inheritance memungkinkan kita untuk mendefinisikan kelas yang 
# mewarisi semua metode dan properti dari kelas induk. Kelas induk atau super atau kelas dasar adalah kelas yang memberikan semua metode dan 
# properti. Kelas anak adalah kelas yang mewarisi dari kelas lain atau kelas induk. Mari kita buat kelas siswa dengan mewarisi dari kelas orang.

class Student(person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.data_orang())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.data_orang())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)


