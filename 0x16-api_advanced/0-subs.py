#!/usr/bin/python3
"""
Module for number_of_subscribers function
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given, the
    function should return 0.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    app_name = '0x16-api_advanced'
    user_name = 'FeelingPsychology300'
    headers = {'User-Agent': f'{app_name}/0.0.1 by /u/{user_name}'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    return response.json().get('data', {}).get('subscribers', 0)
