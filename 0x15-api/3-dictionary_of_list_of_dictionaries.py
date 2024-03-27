#!/usr/bin/python3
""" exports information about employee TODO list progress in json format """
import json
import requests
from sys import argv

if __name__ == "__main__":
    task_dict = {}
    user_dict = {}
    all_employees = {}

    user_data = "https://jsonplaceholder.typicode.com/users"
    # accessing the data of all users
    users = (requests.get(user_data)).json()

    for user in users:
        task_list = []
        # access each users task data
        user_todos = user_data + f"/{user['id']}/todos"

        todo_response = (requests.get(user_todos)).json()
        # creating a list of dicionaries of task info for each user
        for item in todo_response:
            task_dict = {"username": user['username'], "task": item["title"],
                         "completed": item['completed']}
            task_list.append(task_dict)
        # update master dictionary
        all_employees[user['id']] = task_list

    with open(f"todo_all_employees.json", 'w') as file:
        json.dump(all_employees, file)
