import os
import requests


def call():
    url = os.environ.get("URL")
    print(url)
    if url is None:
        url = "https://pahadilala.com"

    final_url ="{}/admin/{}".format(url, "login.php")
    print(final_url)
    data = requests.get(final_url)
    print(data.text)

call()