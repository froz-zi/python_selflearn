print('I hope everyone is enjoying the Python Challenge.\nAre you ?')  # jeda baris
print('Days\tTopics\tExercises')  # menambahkan ruang tab atau 4 spasi
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)')  # Untuk menulis garis miring terbalik
print('In every programming language it starts with \"Hello, World!\"')

# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# language = 'Python'
# formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
# print(formated_string)


# String dan angka
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)  # 2 mengacu pada 2 angka penting setelah titik

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string)  # "Berikut ini adalah pustaka python:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))  # membatasinya menjadi dua digit setelah desimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area)  # 2 digit setelah desimal
print(formated_string)

a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

language = 'Python'
pto = language[0:6:2] #
print(pto)  # Pto

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())  # 'tiga puluh hari ular piton'
print(challenge.expandtabs(10))  # 'tiga puluh hari ular piton'

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9))  # kesalahan