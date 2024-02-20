#!/usr/bin/python3
"""
script that uses the https://jsonplaceholder.typicode.com/ REST API,
for a given employee ID, returns information about his/her TODO list
progress and extend script to export data in the CSV format
"""
import requests

import sys

# if __name__ == '__main__':
#     user = sys.argv[1]
#     url_user = 'https://jsonplaceholder.typicode.com/users/' + user
#     res = requests.get(url_user)
#     """ANYTHING"""
#     user_name = res.json().get('username')
#     task = url_user + '/todos'
#     res = requests.get(task)
#     tasks = res.json()

#     with open('{}.csv'.format(user), 'w') as csvfile:
#         for task in tasks:
#             completed = task.get('completed')
#             """Complete"""
#             title_task = task.get('title')
#             """Done"""
#             csvfile.write('"{}","{}","{}","{}"\n'.format(
#                 user, user_name, completed, title_task))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        REST_API = "https://jsonplaceholder.typicode.com/"
        if isinstance(sys.argv[1].isnumeric(), int):
            user_id = int(sys.argv[1])
            user = requests.get(f"{REST_API}users/{user_id}", timeout=5).json()
            user_tasks = requests.get(
                f"{REST_API}users/{user_id}/todos", timeout=5).json()

            csv_file = f"{user_id}.csv"
            with open(csv_file, 'w', encoding="utf-8") as c_file:
                for task in user_tasks:
                    list_format = f"\"{user_id}\",\"{user['username']}\",\""
                    list_format += f"{task['completed']}\",\"{task['title']}"
                    list_format += "\"\n"
                    c_file.write(list_format)
