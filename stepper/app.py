from flask import Flask
import mysql.connector
import requests
import json
import time
from time import sleep


# mydb = mysql.connector.connect(
#     host="weldpi",
#     user="root",
#     password="Qwertyuioplmn-12"
# )

# Variable assignment
ip = 'http://192.168.188.137:8080/'


app = Flask(__name__)

@app.route('/')
def home():
    return 'First page'

# @app.route('/')
# def home():
#     return 'Hello, World!'

# @app.route('/')
# def home():
#     return 'Hello, World!'

# @app.route('/')
# def home():
#     return 'Hello, World!'

# @app.route('/')
# def home():
#     return 'Hello, World!'

# @app.route('/')
# def home():
#     return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
