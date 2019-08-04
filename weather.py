import requests

api_server = "https://api.weather.yandex.ru/v1/forecast?"
headers = {"X-Yandex-API-Key": "token"}

def main(location):
    ll = str(location)
    x = ll[14:23]
    y = ll[37:46]
    coordinates = {'lat': x, 'lon': y, 'lang': 'ru_RU'}
    r = requests.get('https://api.weather.yandex.ru/v1/forecast?', headers=headers, params=coordinates)
    json_r = r.json()
    weather = json_r['fact']
    temp = str(weather['temp'])
    condition = str(weather['condition'])

    if condition == 'clear':
        condition = ' ясно.'
    elif condition == 'partly-cloudy':
        condition = ' малооблачно.'
    elif condition == 'cloudy':
        condition = ' облачно с прояснениями.'
    elif condition == 'overcast':
        condition = ' пасмурно.'
    elif condition == 'partly-cloudy-and-light-rain':
        condition = ' небольшой дождь.'
    elif condition == 'partly-cloudy-and-rain':
        condition = ' дождь.'
    elif condition == 'overcast-and-rain':
        condition = ' сильный дождь.'
    elif condition == 'overcast-thunderstorms-with-rain':
        condition = ' сильный дождь, гроза.'
    elif condition == 'cloudy-and-light-rain':
        condition = ' небольшой дождь.'
    elif condition == 'overcast-and-light-rain':
        condition = ' небольшой дождь.'
    elif condition == 'cloudy-and-rain':
        condition = ' дождь.'
    elif condition == 'overcast-and-wet-snow':
        condition = ' дождь со снегом.'
    elif condition == 'partly-cloudy-and-light-snow':
        condition = ' небольшой снег.'
    elif condition == 'partly-cloudy-and-snow':
        condition = ' снег.'
    elif condition == 'overcast-and-snow':
        condition = ' снегопад.'
    elif condition == 'cloudy-and-light-snow':
        condition = ' небольшой снег.'
    elif condition == 'overcast-and-light-snow':
        condition = ' небольшой снег.'
    elif condition == 'cloudy-and-snow':
        condition = ' снег.'

    res = 'В твоей местности сейчас ' + temp + '°C,' + condition
    return res