from flask import Flask, render_template, redirect, request, session,  url_for
import requests
import asyncio
import time
from aiohttp import ClientSession
import requests
import os
import string
import re

h = string.ascii_uppercase
u = string.ascii_lowercase

cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']

session = requests.Session()
activ_sess=[]
def pict(pic):
    res = requests.get('https://randomfox.ca/floof/')
    d = res.json()
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

BASE_DIR = os.path.dirname(__name__)

app = Flask(__name__)

app.config['SECRET_KEY']= 'my secret key 12324141 fssdds'
r_num = 0

users=['user1', 'user22', 'user333', 'suer4', 'user55', 'user6666']
user={'user1':{'password':'1234AbAb', 'name':'ППП'}}

@app.route("/count/")
def count():
    # global r_num
    if not 'num' in session:
        session['num'] = 0
        
    session['num'] += 1
    return render_template('count.html', num=session['num'])

   
@app.route("/regest/", methods=['GET', 'POST'])
def rendex():
    error= ''
    login = ''
    pas = ''
    name = ''
    age = 18
    if request.method == 'POST':
        login= request.form.get('login')
        name= request.form.get('name')
        pas = request.form.get('password')
        #age= request.form.get('age')
        #print('login', 'age', 'password', 'name')
        if int(age)>12 and int(age)<100 and any(char in h for char in list(str(pas))):
            user[login]={'name':name, 'password':pas}
            users.append(login)
            return  render_template('vhod.html')
        else:

            error = "Не верный пароль"
    return render_template('regest.html', errror = error, login=login, name=name)

@app.route("/vhod/", methods=['GET', 'POST'])
def vndex():
    error= ''
    login = ''
    pas=''
    if request.method == 'POST':
        login= request.form.get('login')
        pas = request.form.get('password')
        if login in users and user[login]['password']==pas:
            return redirect(url_for('index'))
        else:
            error = "Не верный пароль"
    return render_template('vhod.html')

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