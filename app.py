from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/permissions', methods=['POST'])
def permissions():
    audio = request.form['audio'] == 'true'
    video = request.form['video'] == 'true'
    devices = request.form['devices']
    send_permissions(audio, video, devices)
    return 'OK'

@app.route('/location', methods=['POST'])
def location():
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    send_location(latitude, longitude)
    return 'OK'

def send_permissions(audio, video, devices):
    # сохраняем информацию в текстовый файл по пунктам
    with open('information.txt', 'a') as f:
        f.write('1. Audio: {}\n2. Video: {}\n3. Devices:\n{}\n'.format('Allowed' if audio else 'Denied', 'Allowed' if video else 'Denied', devices))

def send_location(latitude, longitude):
    # сохраняем информацию в текстовый файл по пунктам
    with open('information.txt', 'a') as f:
        f.write('4. Latitude: {}\n   Longitude: {}\n'.format(latitude, longitude))

if __name__ == '__main__':
    app.run()