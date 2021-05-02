import requests


def get_url_status(urls):  # checks status for each url in list urls
    # for url in urls:
    try:
        r = requests.get(urls)
        print(urls + "\tStatus: " + str(r.status_code)) # Prints the url and status of the site(Up/Down)
    except Exception as e:
        print(urls + " - The url is probably down or isn't written correctly. Make sure to add http or https. ")


def main():
    url = input("Enter a full URL 'https://yoursite.com': ")
    get_url_status(url)


if __name__ == "__main__":
    main()
