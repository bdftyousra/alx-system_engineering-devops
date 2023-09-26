#!/usr/bin/python3
"""
Task 0 - Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    rq = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                      format(argv[1]))
    rqname = rq.json().get('name')

    rq = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                      format(argv[1]))
    rqdata = rq.json()
    done = total = 0
    for task in rqdata:
        total += 1
        if task.get('completed'):
            done += 1

    print('Employee {} is done with tasks({}/{}):'.format(rqname, done, total))
    for task in rqdata:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
