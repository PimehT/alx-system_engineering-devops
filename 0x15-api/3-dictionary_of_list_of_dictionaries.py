#!/usr/bin/python3
import requests
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f'{url}/users').json()
    formatted_data = {}
    for user in users:
        user_id = user['id']
        user_name = user['username']
        todos = requests.get(f'{url}/todos').json()
        user_todos = [task for task in todos if task.get('userId') == user_id]
        formatted_todos = [{
            "username": user_name,
            "task": task.get('title'),
            "completed": task.get('completed')
        } for task in user_todos]
        formatted_data[user_id] = formatted_todos
    with open('todo_all_employees.json', 'w') as file:
        json.dump(formatted_data, file, indent=4)
