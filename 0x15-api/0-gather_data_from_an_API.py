#!/usr/bin/python3``
"""
returns information about his/her TO_DO list progress.
"""
import re
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    if re.fullmatch(r'\d+', argv[1]):
        user_id = int(argv[1])
    user = requests.get(f'{url}/users/{user_id}').json()
    todos = requests.get(f'{url}/todos?userId={user_id}').json()
    completed = [task for task in todos if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completed), len(todos)))
    [print("\t {}".format(task.get('title'))) for task in completed]
