#!/usr/bin/python3
"""
Task 3 - extend your Python script to export data in the JSON format.
"""

if __name__ == '__main__':
    import requests
    import json
    from sys import argv

    ids = set()
    rq = requests.get('https://jsonplaceholder.typicode.com/posts')
    rqdata = rq.json()
    for user in rqdata:
        ids.add(user.get('userId'))

    export = {}
    for user in ids:
        rq = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                          format(user))
        rqname = rq.json().get('username')

        rq = requests.get('https://jsonplaceholder.typicode.com/' +
                          'todos?userId={}'.format(user))
        rqdata = rq.json()

        export['{}'.format(user)] = []
        for task in rqdata:
            export['{}'.format(user)].append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': rqname
            })

    with open('todo_all_employees.json', 'w') as outfile:
        json.dump({int(x): export[x] for x in export.keys()},
                  outfile, sort_keys=True)
