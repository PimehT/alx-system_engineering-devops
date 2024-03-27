#!/usr/bin/python3
"""
returns information about his/her TO_DO list progress.
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

        with open(f'todo_all_employees.json', 'w') as file:
            user_name = user.get('username')
            json.dump({id: [{
                "username": user_name,
                "task": task.get('title'),
                "completed": task.get('completed')
            } for task in todos]}, file)
