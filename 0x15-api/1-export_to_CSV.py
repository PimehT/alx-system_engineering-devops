#!/usr/bin/python3``
"""
returns information about his/her TO_DO list progress.
"""
import csv
import re
import requests
from sys import argv


def export_to_csv(user_id, todos):
    """
    Exports the given todos to a CSV file named after the user_id.
    """
    file_name = f"{user_id}.csv"
    with open(file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([
            "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos:
            csv_writer.writerow([
                user_id, user.get(
                    'username'), task.get('completed'), task.get('title')])


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    if re.fullmatch(r'\d+', argv[1]):
        user_id = int(argv[1])
        user = requests.get(f'{url}/users/{user_id}').json()
        user_name = user.get('name')
        todos = requests.get(f'{url}/todos').json()
        user_todos = [task for task in todos if task.get('userId') == user_id]
        completed = [task for task in user_todos
                     if task.get('completed') is True]
        export_to_csv(user_id, user_todos)
