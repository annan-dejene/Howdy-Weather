import requests, os, load_country
from flask import Flask, request, render_template


app = Flask(__name__)
API_KEY = os.environ['API_KEY']


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    city = request.form.get('city')
    temp, country = temprature_extract(city)

    if temp:
      return render_template('display_temprature.html', temp=temp, city=city, country=load_country.load_country(country))
    
    else:
      return render_template('display_temprature.html', temp=temp, city=city, country=country)
      
  return render_template('index.html')



def temprature_extract(city):
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
  response = requests.get(url)

  if response.status_code == 200:
    resp = response.json()
    temp_cels = round(resp["main"]["temp"] - 273.15, 1)
    country = resp["sys"]["country"]
    return temp_cels, country

  return None, None

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
