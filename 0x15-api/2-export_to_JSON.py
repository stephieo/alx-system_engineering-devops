#!/usr/bin/python3
""" exports information about employee TODO list progress in json format """
import json
import requests
from sys import argv

if __name__ == "__main__":
    # accessing api with user task data
    user_todos = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    todo_response = (requests.get(user_todos)).json()

    # accessing usernames
    user_collection = "https://jsonplaceholder.typicode.com/users/"
    user_data = user_collection + argv[1]
    response = (requests.get(user_data)).json()
    print(response)

    task_list = []
    task_dict = {}
    user_dict = {}

# creating the dicionary to turn to json fomat
    for item in todo_response:
        task_dict = {"task": item["title"], "completed": item['completed'],
                     "username": response['username']}
        task_list.append(task_dict)
    user_dict = {item['userId']: task_list}
    print(user_dict)

    with open(f"{argv[1]}.json", 'w') as file:
        json.dump(user_dict, file)
