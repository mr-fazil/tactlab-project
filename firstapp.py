from flask import Flask, jsonify, request, redirect
from flask_pymongo import PyMongo
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://fazil123:fazil123@cluster0.ml7sf.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
db_enter = db.test


@app.route('/create-many')
def create_many():
    new_user_1 = {'A1':'https://atharvaaingle.medium.com/10-tips-to-learn-machine-learning-72b7dcf15528'}
    new_user_2 = {'A2' :'https://medium.com/@randylaosat/a-beginners-guide-to-machine-learning-dfadc19f6caf'}
    new_user_3 = {'A3' :'https://towardsdatascience.com/apples-new-m1-chip-is-a-machine-learning-beast-70ca8bfa6203'}
    new_users = [new_user_1, new_user_2, new_user_3]
    db_enter.insert_many(new_users)
    result = {'result' : 'Created successfully'}
    return result

if __name__ == '__main__':
    app.run(debug=True)