# importing Flask and other modules
from flask import Flask, request, render_template, jsonify, make_response
import requests

# Flask constructor
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def homepage():
    return render_template("index.html")


@app.route('/data')
def data():
    if request.method == 'GET':
        return render_template('data.html')


if __name__ == '__main__':
    app.run()
