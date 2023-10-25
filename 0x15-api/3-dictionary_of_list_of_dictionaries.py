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
    api_endpoint = "https://jsonplaceholder.typicode.com/{}"
    employee_list = req.get(api_endpoint.format('users')).json()
    todos_endpoint = api_endpoint.format("todos")

    employee_dict = {}

    for user in employee_list:
        employee_id = str(user.get('id'))
        username = user.get('username')
        user_todos = "{}?userId={}".format(todos_endpoint, employee_id)
        employee_todos = req.get(user_todos).json()

        employee_todo_list = []
        for todo in employee_todos:
            employee_todo_list.append({
                "username": username,
                "task": todo.get('title'),
                "completed": todo.get('completed'),
            })

        employee_dict[employee_id] = employee_todo_list

    with open("todo_all_employees.json", 'w') as file:
        json.dump(employee_dict, file)
