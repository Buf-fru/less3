from flask import Flask, render_template
import requests
import asyncio
import time
from aiohttp import ClientSession
import requests

cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']


def pict(pic):
    res= requests.get('')
    d= res.json(pic)
    return d['image']

def get_weather(city):    
    '''
    синхронная функция получения погоды
    '''
    url = f'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}
    res = requests.get(url, params)
    res = res.json()     
    return f'{city}: {res["weather"][0]["main"]}'


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('kik.html')

@app.route("/duck/")
def deck():
    #utk= pict("https://random-d.uk/api/images/51.jpg")
    return render_template('duck.html')

@app.route("/fox/<int:num>")
def fex(num):
    w= []
    if num>=1 and num<=10:
        return render_template('fox.html', numb=num)
    else:
        return '<h2 style="color:red">такой страницы не существует</h2>'
@app.route("/weather-minsk/")
def dex():
    h=get_weather('minsk')
    return  render_template('mins.html', hi=h)

@app.route("/weather/<city>/")
def wdex(city):
    j=get_weather(city)
    return render_template('gorod.html', ji=j)

@app.errorhandler(404)
def page_not_found(error):
    return '<h2 style="color:red">такой страницы не существует</h2>'

app.run(debug=True)