import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getstatus', methods=['POST'])
def get_url_status(urls):  # checks status for each url in list urls
    variable = request.form['urls']
    # for url in urls:
    try:
        r = requests.get(urls)
        print(urls + "\tStatus: " + str(r.status_code))
    except Exception as e:
        print(urls + "\tNA FAILED TO CONNECT\t" + str(e))


def main():
    url = input("Text: ")
    get_url_status(url)


if __name__ == "__main__":
    app.run(port=5000, host="localhost")
    main()
