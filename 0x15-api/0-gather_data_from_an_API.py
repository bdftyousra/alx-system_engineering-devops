#!/usr/bin/python3
<<<<<<< HEAD
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    json_o = res.json()
    print("Employee {} is done with tasks".format(json_o.get('name')), end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        if task.get('completed') is True:
            l_task.append(task)

    print("({}/{}):".format(len(l_task), len(tasks)))
    for task in l_task:
        print("\t {}".format(task.get("title")))
=======
'''
Python script that returns information using REST API
'''
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(url, user))
        name = req.json().get("name")
        if name is not None:
            jreq = requests.get(
                "{}todos?userId={}".format(
                    url, user)).json()
            alltsk = len(jreq)
            completedtsk = []
            for t in jreq:
                if t.get("completed") is True:
                    completedtsk.append(t)
            count = len(completedtsk)
            print("Employee {} is done with tasks({}/{}):"
                  .format(name, count, alltsk))
            for title in completedtsk:
                print("\t {}".format(title.get("title")))
>>>>>>> 8babac2a267dd0918195e79dbb5fba38c8d6b656
