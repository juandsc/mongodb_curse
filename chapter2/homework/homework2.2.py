#!/usr/bin/env python
import pymongo


def find():
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.students
    grades = db.grades

    query = {'type': 'homework'}

    try:
        cursor = grades.find(query).sort([('student_id', pymongo.ASCENDING),
                                         ('score', pymongo.ASCENDING)])

        student_id = -1
        count = 0
        for doc in cursor:
            if doc['student_id'] != student_id:
                student_id = doc['student_id']
                _id = doc['_id']
                grades.delete_one({'_id': _id})
    except Exception as e:
        print("Unexpected error:", type(e), e)


if __name__ == '__main__':
    find()  # Change this to find_one() to run that function, instead.
