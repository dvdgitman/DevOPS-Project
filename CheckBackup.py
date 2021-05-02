# importing Flask and other modules
from flask import Flask, request, render_template
import cgi
import requests
import webbrowser

form = cgi.FieldStorage()
# Flask constructor
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def homepage():
    """Run a web UI."""
    return render_template("index.html")


@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == "GET":
        return ()
        site = form.getvalue('name')
        #url = requests.get(site)
        return render_template('data.html')
        #print(site.status_code)
    # if request.get != 'url':
    #     return render_template('url.html')


if __name__ == '__main__':
    app.run(debug=True)
