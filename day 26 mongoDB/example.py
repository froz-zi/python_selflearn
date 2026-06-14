# # let's import the flask
# from flask import Flask, render_template
# import os # importing operating system module
# MONGODB_URI = 'mongodb+srv://froz:froz@cluster0.mbj0vyh.mongodb.net/?appName=Cluster0'
# client = pymongo.MongoClient(MONGODB_URI)
# print(client.list_database_names())

# app = Flask(__name__)
# if __name__ == '__main__':
#     # for deployment we use the environ
#     # to make it work for both production and development
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)


# from flask import Flask
# import pymongo
# import os

# let's import the flask
from flask import Flask, render_template
import os
import pymongo

# MONGODB_URI = variabel buatan kita
# Ganti PASSWORD_KAMU dengan password database user MongoDB kamu
MONGODB_URI = "mongodb+srv://froz:froz@cluster0.mbj0vyh.mongodb.net/?appName=Cluster0"


client = pymongo.MongoClient(MONGODB_URI)


db = client["belajar_flask"]

# students = list berisi banyak data dictionary
students = [
    {"name": "David", "country": "UK", "city": "London", "age": 34},
    {"name": "John", "country": "Sweden", "city": "Stockholm", "age": 28},
    {"name": "Sami", "country": "Finland", "city": "Helsinki", "age": 25},
]

# memasukkan data satu per satu ke collection students
for student in students:
    db.students.insert_one(student)

# ambil satu data pertama
student = db.students.find_one()
print("Satu data pertama:")
print(student)

# cari data berdasarkan nama
john = db.students.find_one({"name": "John"})
print("Data John:")
print(john)

# ambil semua data
all_students = db.students.find()
print("Semua students:")
for student in all_students:
    print(student)

print("Data students berhasil dimasukkan")
print(client.list_database_names())
print(db.list_collection_names())
students = db.students.find({"name": "David"})

for student in students:
    print(student)


students = db.students.find({"age": 28})

for student in students:
    print(student)

students = db.students.find({"age": {"$gt": 25}})

for student in students:
    print(student)


result = db.students.update_one(
    {"name": "David"},
    {"$set": {"age": 35}}
)

print("Jumlah data yang cocok:", result.matched_count)
print("Jumlah data yang berubah:", result.modified_count)

# cek hasil update
david = db.students.find_one({"name": "David"})
print(david)
result = db.students.delete_one({"name": "John"})

print("Jumlah data yang dihapus:", result.deleted_count)

# cek semua data setelah delete
students = db.students.find()

print("Data students setelah delete:")
for student in students:
    print(student)

# cek collection sebelum dihapus
print("Sebelum drop:")
print(db.list_collection_names())

# hapus collection students
db.students.drop()

print("Collection students berhasil dihapus")

# cek collection setelah dihapus
print("Setelah drop:")
print(db.list_collection_names())




app = Flask(__name__)

@app.route("/")
def home():
    return "Flask dan MongoDB berhasil jalan"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    # use_reloader=False supaya data tidak masuk dobel saat debug
    app.run(debug=True, host="0.0.0.0", port=port, use_reloader=False)