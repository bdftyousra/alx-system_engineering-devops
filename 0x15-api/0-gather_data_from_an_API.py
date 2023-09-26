<<<<<<< HEAD
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Construct the API URL
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Send an HTTP GET request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        todos = response.json()

        # Calculate the number of completed tasks and total tasks
        total_tasks = len(todos)
        completed_tasks = sum(1 for todo in todos if todo['completed'])

        # Get the employee's name
        employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        employee_response = requests.get(employee_url)
        if employee_response.status_code == 200:
            employee_name = employee_response.json()['name']
        else:
            employee_name = 'Unknown'

        # Display the TODO list progress
        print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
        for todo in todos:
            if todo['completed']:
                print(f"\t{todo['title']}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        get_employee_todo_progress(employee_id)

=======
#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = main_url + "/user/{}/todos".format(argv[1])
    name_url = main_url + "/users/{}".format(argv[1])
    todo_result = get(todo_url).json()
    name_result = get(name_url).json()

    todo_num = len(todo_result)
    todo_complete = len([todo for todo in todo_result
                         if todo.get("completed")])
    name = name_result.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, todo_complete, todo_num))
    for todo in todo_result:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
>>>>>>> 9d7a3d748ac20d8e61855bfb73ecb6e9d50a7de0
