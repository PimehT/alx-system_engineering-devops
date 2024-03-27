#!/usr/bin/python3
"""
returns information about his/her TO_DO list progress.
export data to a JSON file.
"""
import json
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
        completed = [task for task in user_todos
                     if task.get('completed') is True]

        with open(f'{id}.json', 'w') as file:
            json.dump({id: [{
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user_name
            } for task in user_todos]}, file)
