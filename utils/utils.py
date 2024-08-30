from datetime import datetime
import json
import os
from tabulate import tabulate
import sys



DBPATH = "./db.json"
data_template = []

def create_database(path):
    if not os.path.exists(path):
        with open(path, "+w", encoding='utf8') as f:
            json.dump(data_template, f)
            return True


def read_data(path) -> list:
    if not os.path.exists(path):
        create_database(path)
   
    json_file = open(path, encoding='utf8')
    database = json.load(json_file)
    json_file.close()
    return database


todo_list = read_data(DBPATH)


def add_work(title, status = "todo"):
    global todo_list

    id = len(todo_list) +1
    work = {
        "id": id,
        "title": title,
        "status": status,
        "createdAt": str(datetime.now()),
        "updatedAt": str(datetime.now())
    }

    todo_list.append(work)
    write_data(todo_list, DBPATH)

    return True

def write_data(data, path):
    with open(path, "+w", encoding='utf8') as f:
        json.dump(data, f, indent='\t')
        return True
    
def delete_work(id):
    global todo_list
    
    for index, work in enumerate(todo_list):
        if work['id'] == id:
            deleted_work = todo_list.pop(index)
            print(f"work {deleted_work["title"]} deleted")
            write_data(todo_list, DBPATH)
            return True
    else:
        print(f"wrong id: {id}")
        return False
    
def mark_in_progress(id):
    global todo_list
    
    for index, work in enumerate(todo_list):
        if work['id'] == id:
            todo_list[index]['status'] = "in_progress"
            write_data(todo_list, DBPATH)
            print("status changed successfully")
            return True
    else:
        print(f"wrong id: {id}")
        return False
    
def mark_done(id):
    global todo_list
    
    for index, work in enumerate(todo_list):
        if work['id'] == id:
            todo_list[index]['status'] = "Done"
            write_data(todo_list, DBPATH)
            print("status changed successfully")
            return True
    else:
        print(f"wrong id: {id}")
        return False
    
def list_all():
    data = []
    for work in todo_list:
        data.append([work['id'], work['title'], work['status'],])
    print(tabulate(data, headers=["id", "title", "status"], tablefmt="simple_grid"))


def list_all_done():
    data = []
    for work in todo_list:
        if work['status'] == "Done":
            data.append([work['id'], work['title'], work['status'],])

    print(tabulate(data, headers=["id", "title", "status"], tablefmt="simple_grid"))

def list_all_in_progress():
    data = []
    for work in todo_list:
        if work['status'] == "in_progress":
            data.append([work['id'], work['title'], work['status'],])

    print(tabulate(data, headers=["id", "title", "status"], tablefmt="simple_grid"))

def list_all_todo():
    data = []
    for work in todo_list:
        if work['status'] == "todo":
            data.append([work['id'], work['title'], work['status'], work['createdAt'], work['updatedAt']])

    print(tabulate(data, headers=["id", "title", "status", "createdAt", "updatedAt"], tablefmt="simple_grid"))


def update_work(id, new_title):
 
    for index, work in enumerate(todo_list):
        if work['id'] == id:
            todo_list[index]["title"] = new_title
            todo_list[index]["updatedAt"] = str(datetime.now())
            write_data(todo_list, DBPATH)
            print("title changed successfully")
            return True
    else:
        print(f"wrong id: {id}")
        return False
    

