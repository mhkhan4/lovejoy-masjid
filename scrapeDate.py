import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

# send an HTTP request to the website
url = 'https://hilalcommittee.org/'
response = requests.get(url)

# parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# find the Hijri date element and extract the date
hijri_date = soup.find('span', {'class': 'IDate'}).text
# print the Hijri date
print(hijri_date)

#hijridate
@app.route('/hijriDate')
def hijriDate():
    # Run your Python code here and return the results
    return hijri_date

#csv file
@app.route('/salahTime')
def salahTime():
    csv_string = ""
    with open('./fixed.csv', 'r') as csv_file:
        csv_string = csv_file.read()
    return csv_string






if __name__ == '__main__':
    app.run()

