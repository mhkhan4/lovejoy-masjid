import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, send_file, jsonify

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    date = {'hijriDate': hijriDate()}
    return render_template('newDesignForLovejoyMasjid.html', date=date)

#hijridate
# @app.route('/hijriDate')
def hijriDate():
    # send an HTTP request to the website
    url = 'https://hilalcommittee.org/'
    response = requests.get(url)

    # parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # find the Hijri date element and extract the date
    hijri_date = soup.find('span', {'class': 'IDate'}).text
    # Run your Python code here and return the results
    return hijri_date

#csv file
@app.route('/salahTime')
def salahTime():
    csv_string = ""
    with open('./fixed.csv', 'r') as csv_file:
        csv_string = csv_file.read()
    data = {'time': csv_string}
    return jsonify(data)

@app.route('/image')
def serve_image():
    return send_file('greenBackground.jpg', mimetype='image/jpg')


if __name__ == '__main__':
    app.run(debug=True)

