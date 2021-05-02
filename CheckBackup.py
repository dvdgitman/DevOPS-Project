# importing Flask and other modules
from flask import Flask, request, render_template, redirect, url_for
import webbrowser

# Flask constructor
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def homepage():
    return render_template("index.html")


@app.route('/data/', methods=['POST', 'GET'])
def data():
    if request.method == "GET":
        url = request.form["url"]
        return redirect(url_for("data"))
    else:
        return render_template('url.html')
    # if request.get != 'url':
    #     return render_template('url.html')




if __name__ == '__main__':
    app.run(debug=True)
