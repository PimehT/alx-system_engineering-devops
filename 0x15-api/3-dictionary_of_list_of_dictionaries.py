#!/usr/bin/python3
"""
returns information about all todo of users.
export data to a JSON file.
"""
import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(f'{url}users/').json()
    todos = requests.get(f'{url}todos/').json()
    tasks = [todo for todo in todos if todo.get('userId') == int(id)]

    json_data = {}
    for user in users:
        id = user.get('id')
        data = [{'username': user.get('username'),
                'task': task.get('title'),
                'completed': task.get('completed')} for task in todos
                if todos.get('userId') == id]
        json_data[id] = data
    with open('todo_all_employees.json', 'w') as file:
        json.dump(json_data, file, indent=4)
