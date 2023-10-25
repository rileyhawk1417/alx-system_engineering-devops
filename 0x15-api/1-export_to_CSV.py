#!/usr/bin/python3
"""
Fetch user id from API, then match it with the todos
After that write to a csv file
"""
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
    user_todos = "{}?userId={}".format(todos_endpoint, employee_id)
    employee_list = req.get(users_endpoint)
    employee_name = employee_list.json().get("name")

    employee_todo = req.get(user_todos)
    todo_list = employee_todo.json()

    with open("{}.csv".format(employee_id), "w") as file:
        # file.write('"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"\n')
        for todo in todo_list:
            file.write(
                '"{}","{}","{}","{}"\n'
                .format(employee_id, employee_name,
                        todo.get("completed"), todo.get("title")
                        )
            )
