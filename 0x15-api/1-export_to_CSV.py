#!/usr/bin/python3``
"""
returns information about his/her TO_DO list progress.
"""
import csv
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
                user_id, user.get('username'), task.get('completed'), task.get('title')])


if __name__ == "__main__":
    user_id = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user = requests.get(url).json()
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        user_id)
    todos = requests.get(url).json()
    export_to_csv(user_id, todos)
