#!/usr/bin/python3``
"""
using this REST API, for a given employee ID,
returns information about his/her TO_DO list progress.
"""

import requests
from sys import argv


def gather_data(user_id):
    """
    Gather data from an API endpoint.
    """
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


if __name__ == "__main__":
    user_id = int(argv[1])
    gather_data(user_id)
