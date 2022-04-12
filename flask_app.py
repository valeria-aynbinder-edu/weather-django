from functools import lru_cache

import boto3
from boto3 import s3
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return get_capital(request.args['country'])


@lru_cache(maxsize=5)
def get_capital(country):
    print("inside get_capital", country)
    s3 = boto3.resource('s3')
    file_obj = s3.Object('valeria123', 'concap.csv')
    for i, line in enumerate(file_obj.get()['Body'].iter_lines()):
        decoded_line = line.decode().split(",")
        if decoded_line[0].lower() == country.lower():
            return decoded_line[1]

if __name__ == "__main__":
    app.run(debug=True, port=4747, host='127.0.0.1')