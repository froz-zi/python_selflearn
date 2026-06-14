#Dummy

# from flask import Flask, Response
# import json
# import os

# app = Flask(__name__)

# @app.route('/api/v1.0/students', methods=['GET'])
# def students():
#     student_list = [
#         {
#             'name': 'Asabeneh',
#             'country': 'Finland',
#             'city': 'Helsinki',
#             'skills': ['HTML', 'CSS', 'JavaScript', 'Python']
#         },
#         {
#             'name': 'David',
#             'country': 'UK',
#             'city': 'London',
#             'skills': ['Python', 'MongoDB']
#         },
#         {
#             'name': 'John',
#             'country': 'Sweden',
#             'city': 'Stockholm',
#             'skills': ['Java', 'C#']
#         }
#     ]

#     return Response(json.dumps(student_list), mimetype='application/json')


# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)



#konek ke mongoDB

# let's import the flask

from flask import Flask, Response, request
import json
import pymongo
import os
from bson.objectid import ObjectId
from bson.errors import InvalidId
from bson.json_util import dumps

app = Flask(__name__)

MONGODB_URI = 'mongodb+srv://froz:froz@cluster0.mbj0vyh.mongodb.net/?appName=Cluster0'

client = pymongo.MongoClient(MONGODB_URI)

db = client['belajar_flask']


# GET semua student
@app.route('/api/v1.0/students', methods=['GET'])
def students():
    student_list = db.students.find()

    return Response(dumps(student_list), mimetype='application/json')


# GET student berdasarkan id
@app.route('/api/v1.0/students/<id>', methods=['GET'])
def single_student(id):
    try:
        student = db.students.find_one({'_id': ObjectId(id)})

        if student is None:
            return Response(
                json.dumps({'message': 'Student not found'}),
                status=404,
                mimetype='application/json'
            )

        return Response(dumps(student), mimetype='application/json')

    except InvalidId:
        return Response(
            json.dumps({'message': 'Invalid student id'}),
            status=400,
            mimetype='application/json'
        )


# GET student berdasarkan nama
@app.route('/api/v1.0/students/name/<name>', methods=['GET'])
def get_student_by_name(name):
    student = db.students.find_one({'name': name})

    if student is None:
        return Response(
            json.dumps({'message': 'Student not found'}),
            status=404,
            mimetype='application/json'
        )

    return Response(dumps(student), mimetype='application/json')


# POST tambah student baru
@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    new_student = request.get_json()

    db.students.insert_one(new_student)

    return Response(
        json.dumps({'message': 'Student created successfully'}),
        status=201,
        mimetype='application/json'
    )


# PUT update student berdasarkan id
@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    try:
        data = request.get_json()

        result = db.students.update_one(
            {'_id': ObjectId(id)},
            {'$set': data}
        )

        if result.matched_count == 0:
            return Response(
                json.dumps({'message': 'Student not found'}),
                status=404,
                mimetype='application/json'
            )

        return Response(
            json.dumps({'message': 'Student updated successfully'}),
            status=200,
            mimetype='application/json'
        )

    except InvalidId:
        return Response(
            json.dumps({'message': 'Invalid student id'}),
            status=400,
            mimetype='application/json'
        )


# DELETE student berdasarkan id
@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student_by_id(id):
    try:
        result = db.students.delete_one({'_id': ObjectId(id)})

        if result.deleted_count == 0:
            return Response(
                json.dumps({'message': 'Student not found'}),
                status=404,
                mimetype='application/json'
            )

        return Response(
            json.dumps({'message': 'Student deleted successfully'}),
            status=200,
            mimetype='application/json'
        )

    except InvalidId:
        return Response(
            json.dumps({'message': 'Invalid student id'}),
            status=400,
            mimetype='application/json'
        )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='localhost', port=port, use_reloader=False)