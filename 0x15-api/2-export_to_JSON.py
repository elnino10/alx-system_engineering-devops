#!/usr/bin/python3
""" Python to get data from an API and convert to Json"""
import json
import requests
import sys

# if __name__ == '__main__':
#     USER_ID = sys.argv[1]
#     url_to_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
#     res = requests.get(url_to_user)
#     """Documentation"""
#     USERNAME = res.json().get('username')
#     """Documentation"""
#     url_to_task = url_to_user + '/todos'
#     res = requests.get(url_to_task)
#     tasks = res.json()

#     dict_data = {USER_ID: []}
#     for task in tasks:
#         TASK_COMPLETED_STATUS = task.get('completed')
#         TASK_TITLE = task.get('title')
#         dict_data[USER_ID].append({
#                                   "task": TASK_TITLE,
#                                   "completed": TASK_COMPLETED_STATUS,
#                                   "username": USERNAME})
#     """print(dict_data)"""
#     with open('{}.json'.format(USER_ID), 'w') as f:
#         json.dump(dict_data, f)

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
