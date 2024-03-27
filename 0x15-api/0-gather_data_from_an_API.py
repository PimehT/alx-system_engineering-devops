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
    todos = requests.get(f'{url}/todos').json()
    todo = [task for task in todos if task.get('userId') == user_id]
    completed = [task for task in todo if task.get('completed')]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completed), len(todo)))
    for task in completed:
        print("\t {}".format(task.get('title')))
