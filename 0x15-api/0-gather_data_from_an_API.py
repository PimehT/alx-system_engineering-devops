#!/usr/bin/python3
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
        user_name = user.get('name')
        todos = requests.get(f'{url}/todos').json()
        user_todos = [task for task in todos if task.get('userId') == user_id]
        completed = [task for task in user_todos
                     if task.get('completed') is True]
        print("Employee {} is done with tasks({}/{}):".format(
            user_name, len(completed), len(user_todos)
        ))
        for task in completed:
            print("\t {}".format(task.get('title')))
