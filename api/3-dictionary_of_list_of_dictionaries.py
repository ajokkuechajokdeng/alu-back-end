#!/usr/bin/python3
""" dictionaries of dictionaries """
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


def outPutJson(Users, Tasks):
    """ Print in terminal output thingy """
    # Output Preparation
    dictJson = dict()
    dictInside = dict()
    listOfDict = []
    for user in Users:
        listOfDict = []
        for task in Tasks:
            dictInside = dict()
            if task["userId"] == user["id"]:
                dictInside["username"] = user["username"]
                dictInside["task"] = task["title"]
                dictInside["completed"] = task["completed"]
                listOfDict.append(dictInside)
        dictJson[user["id"]] = listOfDict

    with open("todo_all_employees.json", mode='w') as f:
        f.write(json.dumps(dictJson))


userLink = "https://jsonplaceholder.typicode.com/users/"
requestPerson = requests.get(userLink)

todoLink = "https://jsonplaceholder.typicode.com/todos/"
requestTodoList = requests.get(todoLink)

searchedUser = requestPerson.json()
listTodoUser = requestTodoList.json()

outPutJson(searchedUser, listTodoUser)
