from flask import Flask, jsonify
import re
import requests
from requests_html import HTMLSession
app = Flask(__name__)

@app.route('/getTimeStories', methods=['GET'])
def get_timesnews():
    URL = "https://time.com/"
    try:
        session = HTMLSession()
        response = session.get(URL)

    except requests.exceptions.RequestException as e:
        print(e)

    section = response.html.find('.swipe-h', first=True).html
    news = [dict() for x in range(5)]
    a = "<a.*?>(.+?)</a>"
    href = r'href=[\'"]?([^\'" >]+)'
    title = re.compile(a)
    address = re.compile(href)
    titles = re.findall(title, section)
    ad = re.findall(address, section)

    for n, data in enumerate(news):
        data['title'] = titles[n]
        data['link'] = ad[2 * n]
    return jsonify({'news': news})




if __name__ == '__main__':
    app.run(debug=True)