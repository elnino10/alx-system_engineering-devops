#!/usr/bin/python3
"""python script to fetch Rest API for todo lists of employees"""

import json

import requests

if __name__ == "__main__":
    REST_API = "https://jsonplaceholder.typicode.com/"
    users = requests.get(f"{REST_API}users/", timeout=10).json()

    todo_dict = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_task_req = requests.get(
            f"{REST_API}/users/{user_id}/todos", timeout=10).json()
        todo_dict[user_id] = []
        for task in user_task_req:
            todo_dict[user_id].append({
                "username": username,
                "task": task["title"],
                "completed": task["completed"],
            })
    JSON_FILE = "todo_all_employees.json"
    with open(JSON_FILE, 'w', encoding="utf-8") as j_file:
        json.dump(todo_dict, j_file)
