
import os
from bson import ObjectId
from flask import Blueprint, make_response, request
from flask import jsonify
from pymongo import MongoClient

mongo_connection_string = os.getenv("MONGO_CONNECTION_STRING")
database_name = os.getenv("MONGO_DATABASE")
collection_name = os.getenv("MONGO_COLLECTION")

client = MongoClient(mongo_connection_string)
db = client[database_name]
collection = db[collection_name]

api = Blueprint('books_api', __name__)

def get_blueprint():
    """Return the blueprint for the main app module"""
    return api

@api.route('/', methods=['GET'])
def get_books():    
    """Return a list of books"""
    books=[]
    docs = collection.find()    
    for item in docs:
        item['_id'] = str(item['_id'])
        books.append(item)
    data = jsonify(books)
    return make_response(data, 200)

@api.route('/', methods=['POST'])
def create_book():
    """Return a list of books"""
    doc = request.get_json()
    result= collection.insert_one(doc)
    resp = {
        'message':'Book detail inserted successfully',
        'id': str(result.inserted_id)
    }
    return make_response(jsonify(resp), 201)

@api.route('/<id>', methods=['GET'])
def get_book_by_id(id):
    book_id = ObjectId(id)
    book = collection.find_one({'_id':book_id}) 
    book['_id'] = str(book['_id'])
    return make_response(jsonify(book), 200)
