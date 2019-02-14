from setuptools import setup

setup(
    name='slackweather',
    version='0.1',
    packages=['slackweather'],
    entry_points={
        'console_scripts':
            ['slackweather = slackweather.auto:set_profile_from_weather']
    }
)
