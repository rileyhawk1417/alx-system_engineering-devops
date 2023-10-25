#!/usr/bin/python3
"""
Fetch user id from API, then match it with the todos
Process the results into a dictionary
Then write to a json file
"""

import json
import requests as req
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    api_endpoint = "https://jsonplaceholder.typicode.com/{}"
    users_endpoint = "{}/{}".format(api_endpoint.format("users"), employee_id)
    todos_endpoint = api_endpoint.format("todos")
    user_todos = "{}?userId={}".format(todos_endpoint, employee_id)
    employee_list = req.get(users_endpoint)
    employee_name = employee_list.json().get("username")

    employee_todo = req.get(user_todos)
    todo_list = employee_todo.json()
    employee_todo_list = []

    employee_dict = {}

    for todo in todo_list:
        employee_todo_list.append({
            "username": employee_name,
            "task": todo.get('title'),
            "completed": todo.get('completed'),
        })

    employee_dict[employee_id] = employee_todo_list

    with open("todo_all_employees.json", 'a') as file:
        json.dump(employee_dict, file)
