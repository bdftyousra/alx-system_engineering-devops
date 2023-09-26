#!/usr/bin/python3
"""
Task 1 - extend your Python script to export data in the CSV format.
"""

if __name__ == '__main__':
    import requests
    import csv
    from sys import argv

    rq = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                      format(argv[1]))
    rqname = rq.json().get('username')

    rq = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                      format(argv[1]))
    rqdata = rq.json()

    with open('{}.csv'.format(argv[1]), mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in rqdata:
            csv_writer.writerow([argv[1], rqname, task.get('completed'),
                                 task.get('title')])
