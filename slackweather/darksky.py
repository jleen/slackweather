import requests

from slackweather import config


def get_weather(where):
    uri = ('https://api.darksky.net/forecast/' +
           config.dark_sky_token + '/' + where)
    if config.debug:
        print(uri)
    r = requests.get(uri)
    return r.json()
