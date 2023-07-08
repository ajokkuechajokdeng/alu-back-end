#!/usr/bin/python3
""" export to CVS """
import csv
import requests
import sys


def verif(request):
    """ check for request status """
    print(request)
    print(request.status_code)
    print(request.headers)
    print(request.text)
    print(request.json())


def outPutCVS(searchedUser, listTodoUser):
    """ Print in terminal output thingy """
    # Output Preparation

    with open("{}.csv".format(searchedUser[0]["id"]), mode='w') as f:
        tasks = csv.writer(f, delimiter=',', quotechar='"',
                           quoting=csv.QUOTE_ALL)

        for task in listTodoUser:
            tasks.writerow([searchedUser[0]["id"],
                            searchedUser[0]["username"],
                            task["completed"],
                            task["title"]])

if len(sys.argv) == 2:
    # Search for person
    userLink = "https://jsonplaceholder.typicode.com/users/"
    id = sys.argv[1]
    queryUser = {'id': id}
    requestPerson = requests.get(userLink, params=queryUser)

    # Search for their respective todo list
    todoLink = "https://jsonplaceholder.typicode.com/todos/"
    queryTodo = {'userId': id}
    requestTodoList = requests.get(todoLink, params=queryTodo)

    searchedUser = requestPerson.json()
    listTodoUser = requestTodoList.json()

    outPutCVS(searchedUser, listTodoUser)

    # tests
    # verif(requestPerson)
    # verif(requestTodoList)
