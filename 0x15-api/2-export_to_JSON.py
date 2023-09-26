#!/usr/bin/python3
"""
Task 2 - extend your Python script to export data in the JSON format.
"""

if __name__ == '__main__':
    import requests
    import json
    from sys import argv

    rq = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                      format(argv[1]))
    rqname = rq.json().get('username')

    rq = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                      format(argv[1]))
    rqdata = rq.json()

    export = {}
    export['{}'.format(argv[1])] = []
    for task in rqdata:
        export['{}'.format(argv[1])].append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': rqname
        })

    with open('{}.json'.format(argv[1]), 'w') as outfile:
        json.dump(export, outfile)
