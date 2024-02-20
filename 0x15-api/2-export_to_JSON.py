#!/usr/bin/python3
""" script to get data from an API and convert and store in json format"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        REST_API = "https://jsonplaceholder.typicode.com/"
        if isinstance(sys.argv[1].isnumeric(), int):
            user_id = int(sys.argv[1])
            user = requests.get(f"{REST_API}users/{user_id}", timeout=5).json()
            user_tasks = requests.get(
                f"{REST_API}users/{user_id}/todos", timeout=5).json()

            my_dict = {user_id: []}
            for task in user_tasks:
                my_dict[user_id].append({
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": user["username"],
                })
            json_file = f"{user_id}.json"
            with open(json_file, 'w', encoding="utf-8") as j_file:
                json.dump(my_dict, j_file)
