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

        users = requests.get(f'{url}/users').json()
        todos = requests.get(f'{url}/todos').json()

        todo_dict = {}
        for user in users:
            user_id = user.get('id')
            user_name = user.get('username')
            user_tasks = [{"username": user_name, "task": task.get('title'), "completed": task.get('completed')} for task in todos if task.get('userId') == user_id]
            todo_dict[user_id] = user_tasks

        with open('todo_all_employees.json', 'w') as file:
            json.dump(todo_dict, file)
