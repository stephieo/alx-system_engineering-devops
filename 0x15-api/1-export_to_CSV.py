#!/usr/bin/python3
""" returns information about employee TODO list progress """
import csv
import requests
from sys import argv

if __name__ == "__main__":
    # accessing api with user task data
    user_todos = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    todo_response = (requests.get(user_todos)).json()

    # accessing username
    user_collection = "https://jsonplaceholder.typicode.com/users/"
    user_data = user_collection + argv[1]
    response = (requests.get(user_data)).json()
    username = response['username']

    # writing to csv file
    with open(f"{argv[1]}.csv", 'w') as file:
        cfile = csv.writer(file, delimiter=',', quotechar='"',
                           quoting=csv.QUOTE_ALL)
        for item in todo_response:
            cfile.writerow([item['userId'], username,
                            item['completed'], item['title']])
