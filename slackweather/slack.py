from slackclient import SlackClient

from slackweather import config


def set_profile(text, emoji):
    sc = SlackClient(config.slack_token)
    sc.api_call('users.profile.set', profile={
            'status_text': text, 'status_emoji': ':' + emoji + ':'})
