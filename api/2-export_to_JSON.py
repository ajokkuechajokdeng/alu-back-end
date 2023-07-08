#!/usr/bin/python3
""" export to json """
import json
import requests
import sys


def verif(request):
    """ check for request status """
    print(request)
    print(request.status_code)
    print(request.headers)
    print(request.text)
    print(request.json())


def outPutJson(searchedUser, listTodoUser):
    """ Print in terminal output thingy """
    # Output Preparation
    dictJson = dict()
    dictInside = dict()
    listOfDict = []
    username = searchedUser[0]["username"]
    for i in range(len(listTodoUser)):
        dictInside = dict()
        dictInside["task"] = listTodoUser[i]["title"]
        dictInside["completed"] = listTodoUser[i]["completed"]
        dictInside["username"] = username
        listOfDict.append(dictInside)

    dictJson[searchedUser[0]["id"]] = listOfDict
    with open("{}.json".format(searchedUser[0]["id"]), mode='w') as f:
        f.write(json.dumps(dictJson))


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

    outPutJson(searchedUser, listTodoUser)

    # tests
    # verif(requestPerson)
    # verif(requestTodoList)
