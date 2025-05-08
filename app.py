import os

import pymongo
from flask import Flask, jsonify
from flask import render_template
from flask import request
from datetime import datetime
app = Flask(__name__)

mongodb_host = os.environ.get('MONGODB_HOST')
mongodb_port = os.environ.get('MONGODB_PORT')
mongodb_username = os.environ.get('MONGODB_USERNAME')
mongodb_password = os.environ.get('MONGODB_PASSWORD')

client = pymongo.MongoClient(mongodb_host, int(mongodb_port), username=mongodb_username, password=mongodb_password)
db = client["devops_sre"]
clicks = db["clicks"]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/clicks', methods=['GET', 'POST'])
def clicks_handler():

    if request.method == 'POST':
        timestamp = int(datetime.now().timestamp())
        # insert the timestamp into db
        clicks.insert_one({'timestamp': timestamp})
        return jsonify({
            'timestamp': timestamp
        }), 200

    if request.method == 'GET':
        #return a list of timestamps out of the db
        timestamps = list(clicks.find({}, {'timestamp': 1, '_id': 0}))
        timestamps = [doc['timestamp'] for doc in timestamps]
        return jsonify({'clicks': timestamps}), 200



