#!/usr/bin/python3
""" gather infos from api """
import requests
import sys


def verif(request):
    """ check for request status """
    print(request)
    print(request.status_code)
    print(request.headers)
    print(request.text)
    print(request.json())

def outPutPrint(searchedUser, listTodoUser):
    """ Print in terminal output thingy """
    # Output Preparation

    if len(searchedUser) != 0:
        EMPLOYEE_NAME = searchedUser[0]["name"]
    else:
        EMPLOYEE_NAME = "Not found"
    NUMBER_OF_DONE_TASKS = str(listTodoUser).count('\'completed\': True')
    TOTAL_NUMBER_OF_TASKS = len(listTodoUser)

    # Output
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in listTodoUser:
        if task["completed"]:
            print("\t {}".format(task["title"]))
    

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

    outPutPrint(searchedUser, listTodoUser)

    # tests
    # verif(requestPerson)
    # verif(requestTodoList)
