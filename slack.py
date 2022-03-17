#!/usr/bin/env python
import json
import requests

credentials = 'credentials.json'
message = '2nd message to a channel'

#https://keestalkstech.com/2019/10/simple-python-code-to-send-message-to-slack-channel-without-packages/#posting-to-a-channel
slack_token = 'xoxp-753891019617-759835025988-2406282880817-1ebc736b9f18a8e15b8c51e2e87108e3'
slack_channel = 'test'
slack_icon_emoji = ':see_no_evil:'
slack_user_name = 'Ram'

def get_credentials(credentials):
    '''
    Read credentials from JSON file.
    '''
    with open(credentials, 'r') as f:
        creds = json.load(f)
    return creds['slack_webhook']

def post_to_slack(message,credentials):
    data = {'text':message}
    url = get_credentials(credentials)
    requests.post(url,json=data, verify=False)

def post_message_to_slack(request, blocks = None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': request["channel"],
        'text': request["message"],
        'icon_emoji': slack_icon_emoji,
        'username': slack_user_name,
        'blocks': json.dumps(blocks) if blocks else None
    }).json()


if __name__ == '__main__':
    #post_to_slack(message,credentials)
    response = post_message_to_slack(message)
    print(response)
