from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=06f05023-dcaa-44ce-bb33-266c4fce79b8"
    req = requests.get(url)
    content = BeautifulSoup(req.content, 'html.parser')

    name = content.find_all('div', {"class": "_4rR01T"})
    price = content.find_all('div', {"class": "_30jeq3 _1_WHN1"})
    rating = content.find_all('div', {"class": "_3LWZlK"})

    nm = []
    pr = []
    rt = []

    for i in name:
        nm.append(i.text)
    for i in price:
        pr.append(i.text)
    for i in range(len(nm)):
        rt.append(rating[i].text)

    return render_template('index.html', names=nm, prices=pr, ratings=rt)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
