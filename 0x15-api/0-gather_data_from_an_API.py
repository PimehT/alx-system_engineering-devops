#!/usr/bin/python3
"""
returns information about his/her TO_DO list progress.
"""
import re
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2 or argv[1].isdigit():
        id = argv[1]
        url = 'https://jsonplaceholder.typicode.com/'
        user = requests.get(url + 'users/' + id).json()
        todos = requests.get(url + 'todos/').json()
        tasks = [todo for todo in todos if todo.get('userId') == int(id)]
        completed = [done for done in tasks if done.get('completed') is True]
        print("Employee {} is done with tasks({}/{}):".format(
            user.get('name'), len(completed), len(tasks)
        ))
        for task in completed:
            print("\t {}".format(task.get('title')))
