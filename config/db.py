from pymongo import MongoClient
conn = MongoClient("mongodb+srv://dorjoohover:dorjooX0@cluster0.lg7cc.mongodb.net/")
db = conn['python_test']
collection = db['user']