import os

FILEPATH = "todos.txt"

if not os.path.exists(FILEPATH):
    with open(FILEPATH, "w") as file:
        pass

def get_todos(filepath = FILEPATH):
    """
    Read a text file and return a list of
    to-do items.
    :param filepath: filepath of .txt file
    :return: list of todos
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_local, filepath = FILEPATH):
    """
     Write a list of to-do items to a text file.
    :param todos_local: list of todos
    :param filepath: filepath of .txt file
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)
