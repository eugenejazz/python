#!/usr/bin/python3

import json
from datetime import datetime
from datetime import timedelta
import sys
import sqlite3
import urllib
import urllib.request
import gzip
import shutil
import os.path

# База данных
bd="ow.bd"

# Получаем app.id из файла
f = open('app.id', 'r')
appid = f.read()
f.close()

# 1. Создавать файл базы данных SQLite со следующей структурой данных
#    (если файла базы данных не существует):

if os.path.exists('{}'.format(bd)):
	print("BD file already exists!")
else:
    # print("BD file not exists!")
    print("Creating database...")
    conn = sqlite3.connect('{}'.format(bd))
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE weather
                      (id_city INTEGER PRIMARY KEY, city VARCHAR(255), date DATE,
                      temp INTEGER, id_wheather INTEGER)
                   """)
    conn.close()

# 2. Выводить список стран из файла и предлагать пользователю выбрать страну 

# получение файла

print("Updating city list...")
destination = 'city.list.json.gz'
url = 'http://bulk.openweathermap.org/sample/city.list.json.gz'
urllib.request.urlretrieve(url, destination)

# распаковка файла

print("Unpacking new city list...")
with gzip.open('city.list.json.gz', 'rb') as f_in:
    with open('city.list.json', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# парсим json в словарь

with open('city.list.json', 'r') as f:
    city_dict = json.load(f)

# получаем уникальные коды стран преобразуя словарь в набор

output = set()
for x in city_dict:
    output.add(x['country'])

# печатаем все коды стран

print("Available country codes:")

for y in output:
    print(y,end = ' ')
print()

countrycod = input('Input country code: ')

# 3. Скачивать JSON (XML) файлы погоды в городах выбранной страны

for city in city_dict:
    if countrycod == city['country']:
        print("Downloading JSON for ", city['name'])
        cityid = city['id']
        destination = 'weatherfiles/%s' % cityid
        url = 'http://api.openweathermap.org/data/2.5/weather?id=%s&units=metric&appid=%s' % (cityid, appid)
        urllib.request.urlretrieve(url, destination)
    else:
        pass


# 4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
#    данных. Если данные для данного города и данного дня есть в базе - обновить
#    температуру в существующей записи.
print("Insert data to database...")
for json_file in os.listdir(path="weatherfiles/"):
    # print(json_file)
        if not json_file.startswith("."):
            # print(json_file)
            with open('weatherfiles/{}'.format(json_file), 'r') as f:
                json_file_dict = json.load(f)
                # print(json_file_dict)
                mainid = json_file
                city = json_file_dict["name"]
                date = str(datetime.now())
                weatherid = json_file_dict['weather'][0]['id']
                temp = json_file_dict['main']['temp']
                # print(mainid)
                # print(city)
                # print(date)
                # print(temp)
                # print(weatherid)
                conn = sqlite3.connect('{}'.format(bd))
                cursor = conn.cursor()
                cursor.execute('insert or replace into weather (id_city, city, date, temp, id_wheather) values("{}", "{}", "{}", "{}", "{}")'.format(mainid, city, date, temp, weatherid))
                conn.commit()
                conn.close()

