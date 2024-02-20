#!/usr/bin/python3
"""
script that uses the https://jsonplaceholder.typicode.com/ REST API,
for a given employee ID, returns information about his/her TODO list
progress
"""
import requests

import sys

REST_API = "https://jsonplaceholder.typicode.com/"
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if isinstance(sys.argv[1].isnumeric(), int):
            user_id = int(sys.argv[1])
            user = requests.get(f"{REST_API}users/{user_id}", timeout=5).json()
            user_tasks = requests.get(
                f"{REST_API}users/{user_id}/todos", timeout=5).json()
            tasks_number = len(user_tasks)
            completed_tasks = len(
                [task for task in user_tasks if task["completed"] is True])
            print(
                f"Employee {user['name']} is done with "
                f"({completed_tasks}/{tasks_number}):"
                )
            for task in user_tasks:
                if task["completed"] is True:
                    print(f"\t {task['title']}")
