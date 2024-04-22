#!/usr/bin/python3
"""
returns information about his/her TO_DO list progress.
export data to a JSON file.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2 or argv[1].isdigit():
        id = argv[1]
        url = 'https://jsonplaceholder.typicode.com/'
        user = requests.get(f'{url}users/{id}').json()
        todos = requests.get(f'{url}todos/').json()
        tasks = [todo for todo in todos if todo.get('userId') == int(id)]
        completed = [done for done in tasks if done.get('completed') is True]

        with open(f'{id}.json', 'w') as file:
            json.dump({id: [{
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user.get('name'),
            } for task in tasks]}, file)
