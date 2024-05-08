#!/usr/bin/python3
"""
Top Ten popular posts of a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Top Ten popular posts of a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Python/requests:APIproject:0.1 (by /u/vegaisaias)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    try:
        data = response.json().get('data').get('children')
        for post in data:
            print(post.get('data').get('title'))
    except Exception:
        print(None)
        return