#!/usr/bin/python3
"""
returns export data in the CSV format of
information about his/her TO_DO list progress.
"""
import csv
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

        with open(f'{id}.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for task in tasks:
                writer.writerow([
                    id,
                    user.get('username'),
                    task.get('completed'),
                    task.get('title')
                ])
