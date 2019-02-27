import time

from slackweather import config
from slackweather import darksky
from slackweather import slack


DEFAULT_STATUS = 'sunny'
NIGHT_STATUS = 'last_quarter_moon_with_face'

CONDITIONS = { 'Thunderstorm': 'thunder_cloud_and_rain',
               'cloudy': 'cloud',
               'partly-cloudy-day': 'mostly_sunny',
               'rain': 'umbrella_with_rain_drops',
               'snow': 'snowflake',
               'partly-cloudy-night': NIGHT_STATUS }

def get_emoji_for_weather(weather):
    now = time.time()

    condition = weather['currently']['icon']
    temperature = weather['currently']['temperature']
    humidity = weather['currently']['humidity']
    sunrise = weather['daily']['data'][0]['sunriseTime']
    sunset = weather['daily']['data'][0]['sunsetTime']

    if config.debug:
        print('Condition: ' + condition)
        print('Temperature: ' + str(temperature))
        print('Humidity: ' + str(humidity))
        print()
        print('Sunrise: ' + str(sunrise))
        print('Sunset: ' + str(sunset))
        print('Now: ' + str(now))

    if now < sunrise or now > sunset:
        return NIGHT_STATUS
    else:
        return CONDITIONS.get(condition, DEFAULT_STATUS)


def set_profile_from_weather():
    location = config.location
    location_name = config.location_name
    weather = darksky.get_weather(location)
    emoji = get_emoji_for_weather(weather)
    slack.set_profile(location_name, emoji)
