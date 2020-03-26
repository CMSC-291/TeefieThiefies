import os

import requests
from bs4 import BeautifulSoup

FILENAME = "teefies.html"

if __name__ == '__main__':
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            html = f.read()
    else:
        html = requests.get("https://old.reddit.com/r/teefies/").text
        with open(FILENAME, 'w') as f:
            f.write(html)

    soup = BeautifulSoup(html, 'html.parser')
    print(soup.select("a")[0].text)

    images = {}
    for img in soup.select("div.thing"):
        url = img.attrs["data-url"]
        title = img.select(".title")[0].text
        images[url] = {
            "title": title,
        }

    with open("thievedteeves.html", 'w') as f:
        lines = []
        for img, data in images.items():
            lines.append('<h3>{}</h3><img style="height:200px" src={} /><br/>'.format(data["title"], img))
        print(lines)
        f.writelines(lines)