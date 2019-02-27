import os


slack_token = os.environ['SLACKWEATHER_SLACK_API_TOKEN']
dark_sky_token = os.environ['SLACKWEATHER_DARK_SKY_API_TOKEN']
location = os.environ['SLACKWEATHER_LOCATION']
location_name = os.environ['SLACKWEATHER_LOCATION_NAME']
debug = os.environ.get('SLACKWEATHER_DEBUG', None)
