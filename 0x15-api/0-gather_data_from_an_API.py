#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)
    user = response.json()
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        user_id)
    response = requests.get(url)
    todos = response.json()
    completed = [task for task in todos if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completed), len(todos)))
    [print("\t {}".format(task.get('title'))) for task in completed]
