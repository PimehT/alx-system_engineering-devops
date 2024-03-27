#!/usr/bin/python3
"""
returns information about his/her TO_DO list progress.
"""
import json
import requests


def export_all_to_json():
    """
    Exports all tasks from all employees to a JSON file.
    """
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    user_dict = {}
    for user in users:
        user_id = user.get('id')
        user_name = user.get('username')
        user_tasks = []
        for task in todos:
            if task.get('userId') == user_id:
                user_tasks.append({
                    "username": user_name,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                })
        user_dict[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_dict, json_file)


if __name__ == "__main__":
    export_all_to_json()
