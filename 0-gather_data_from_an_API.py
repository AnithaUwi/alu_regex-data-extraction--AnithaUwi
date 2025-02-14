#!/usr/bin/python3
pip install requests

import requests
import sys

def gather_data_from_api(employee_id):
    """Fetches employee TODO list progress from the API."""
    # Base URL for the API
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Send GET request to the API to retrieve the TODO list
    response = requests.get(todos_url)
            
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error fetching TODO list for employee ID {employee_id}")
        return
    # Extract the JSON data from the response
    todos = response.json()

    # Get the employee information (name)
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print(f"Error fetching employee info for ID {employee_id}")
        return
    employee_info = employee_response.json()
    employee_name = employee_info.get('name', 'Unknown')

    # Count the completed and total tasks
    completed_tasks = [task['title'] for task in todos if task['completed']]
    total_tasks = len(todos)
    completed_count = len(completed_tasks)

    # Output the employee's progress
    print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        gather_data_from_api(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")

