import csv
import json
from urllib import request
import urllib.request
import time
import datetime as d

datefile = 'dht11_jeu_' + str(d.datetime.now().date()) + '.csv'

with open(datefile, "a+") as file_object:
    fieldnames = ['date', 'time', 'temp', 'humidity']
    spamwriter = csv.DictWriter(file_object, fieldnames=fieldnames)
    spamwriter.writeheader()


while open("command.txt", 'r').read() != "stop":

    date = 'dht11_jeu_' + str(d.datetime.now().date()) + '.csv'
    with open(date, "a+") as file_object:

        fieldnames = ['date', 'time', 'temp', 'humidity']
        spamwriter = csv.DictWriter(file_object, fieldnames=fieldnames)

        url = "http://192.168.1.60:8080/json.htm?username=ZXZhbg===&password=ZXZubw===&type=devices&rid=3"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        data = data["result"]
        data = data[0]

        currentDT = d.datetime.now()


        """file_object.write("à",currentDT.date(), currentDT.time(), "la temprerature vaut: ", data["Temp"])
        file_object.write("à",currentDT.date(), currentDT.time(), "l'humidité vaut: ", data["Humidity"])"""


        spamwriter.writerow({'date': str(currentDT.date()), 'time': str(currentDT.time()),'temp': str(data["Temp"]), 'humidity': data["Humidity"]})

        print("à",currentDT.date(), currentDT.time(), "la temprerature vaut: ", data["Temp"])
        print("à",currentDT.date(), currentDT.time(), "l'humidité vaut: ", data["Humidity"])

        filename = "command.txt"
        open(filename, 'r').read()

        time.sleep(10)
