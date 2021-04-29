import requests

<<<<<<< HEAD
def index():
    return render_template('index.html')

=======
>>>>>>> 5d9552bebcc883f523851c1f46c246e5f4578551

def get_url_status(urls):  # checks status for each url in list urls

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
    main()
