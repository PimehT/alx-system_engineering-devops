"""
returns information about his/her TO_DO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    user_id = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(f'{url}/users/{user_id}').json()
    todos = requests.get(f'{url}/todos?userId={user_id}').json()
    completed = [task for task in todos if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completed), len(todos)))
    [print("\t {}".format(task.get('title'))) for task in completed]
