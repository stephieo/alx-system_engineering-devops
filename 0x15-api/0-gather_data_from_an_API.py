#!/usr/bin/python3
""" returns information about employee TODO list progress """
from sys import argv
import requests

if __name__ == "__main__":
    #api_url = "https://jsonplaceholder.typicode.com/todos/"

    #full_url = api_url + argv[1]


    #response = requests.get(full_url)
    #print(response)
    #response2 = requests.get("https://jsonplaceholder.typicode.com/users/3")
    #print(response2.json())
    #response.dict = response.json()
    #print(response.dict)
    user_collection = "https://jsonplaceholder.typicode.com/users/"
    if argv[1]:
        user_data = user_collection + argv[1]

    response = (requests.get(user_data)).json()
    EMPLOYEE_NAME = response['name']

    user_todos = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    todo_response = (requests.get(user_todos)).json()

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    for item in todo_response:
        if item['completed'] == True:
            NUMBER_OF_DONE_TASKS += 1
        TOTAL_NUMBER_OF_TASKS += 1

    print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for item in todo_response:
        if item['completed'] == True:
            print(f"\t{item['title']}")
    #NUMBER_OF_DONE_TASKS = todo_response[]
    #fetch(full_url)
    #      .then(response => response.json())
    #      .then(json => console.log(json))
