#!/usr/bin/python3
"""
returns export data in the CSV format of
information about his/her TO_DO list progress.
"""
import re
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    if re.fullmatch(r'\d+', argv[1]):
        id = int(argv[1])

        user = requests.get(f'{url}/users/{id}').json()
        todos = requests.get(f'{url}/todos').json()

        user_name = user.get('username')
        user_todos = [task for task in todos if task.get('userId') == id]

        with open(f'{id}.csv', 'w') as file:
            for task in user_todos:
                task_status = task.get('completed')
                task_title = task.get('title')
                file.write('"{}","{}","{}","{}"\n'.format(
                    id, user_name, task_status, task_title
                ))
