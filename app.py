from flask import Flask, jsonify, request, redirect
from flask_pymongo import PyMongo
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://fazil123:fazil123@cluster0.ml7sf.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
db_enter = db.test

@app.route('/create')
def create():
    new_user = {'1.' : 'https://atharvaaingle.medium.com/10-tips-to-learn-machine-learning-72b7dcf15528', }
    db_enter.insert_one(new_user)
    result = {'result' : 'Created successfully'}
    return result
 
if __name__ == '__main__':
    app.run(debug=True)
