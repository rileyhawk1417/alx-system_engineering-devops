#!/usr/bin/python3

import requests as req
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    api_endpoint = "https://jsonplaceholder.typicode.com/{}"
    users_endpoint = "{}/{}".format(api_endpoint.format("users"), employee_id)
    todos_endpoint = api_endpoint.format("todos")

    employee_list = req.get(users_endpoint)
    employee_name = employee_list.json().get("name")

    employee_todo = req.get(todos_endpoint)
    todo_list = employee_todo.json()

    completed = 0
    completed_todos = []

    for todo in todo_list:
        if todo.get("completed"):
            completed_todos.append(todo)
            completed += 1

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, completed, len(todo_list)
        )
    )

    for todo in completed_todos:
        print("\t {}".format(todo.get("title")))
