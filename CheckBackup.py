# importing Flask and other modules
from flask import Flask, request, render_template
import requests

# Flask constructor
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def homepage():
    return render_template("index.html")

@app.route('/data')
def data():
    return render_template('test.html')


if __name__ == '__main__':
    app.run()
