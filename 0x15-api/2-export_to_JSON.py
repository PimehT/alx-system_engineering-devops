#!/usr/bin/python3``
"""
returns information about his/her TO_DO list progress.
"""
import json
import requests
from sys import argv


def export_to_json(user_id, todos):
    """
    Exports the given todos to a JSON file named after the user_id.
    """
    file_name = "{}.json".format(user_id)
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    user_name = user.get('username')
    user_tasks = []
    for task in todos:
        user_tasks.append({"task": task.get('title'),
                           "completed": task.get('completed'),
                           "username": user_name})
    user_dict = {user_id: user_tasks}
    with open(file_name, 'w') as json_file:
        json.dump(user_dict, json_file)


if __name__ == "__main__":
    user_id = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user = requests.get(url).json()
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        user_id)
    todos = requests.get(url).json()
    export_to_json(user_id, todos)
