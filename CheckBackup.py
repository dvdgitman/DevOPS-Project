# importing Flask and other modules
from flask import Flask, request, render_template, jsonify, make_response
import requests

# Flask constructor
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def homepage():
    return render_template("index.html")


@app.route('/data')
def data(urls):
    if request.method == 'GET':
        try:
            r = requests.get(urls)
            print(urls + "\tStatus: " + str(r.status_code))  # Prints the url and status of the site(Up/Down)
        except Exception as e:
            print(urls + " - The url is probably down or isn't written correctly.Make sure to add http or https. ")
        return render_template('data.html')
    # if request.method != 'GET':
    #     return render_template('url.html')


if __name__ == '__main__':
    app.run(debug=True)
