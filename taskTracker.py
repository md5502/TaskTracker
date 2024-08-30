import fire
from utils.utils import list_all_todo, update_work, add_work, delete_work, list_all, mark_done, mark_in_progress, list_all_done, list_all_in_progress


def add(title):
    """
    Adds a new task with the given title.
    """
    if not title:
        return "Title cannot be empty"
    
    if add_work(title):
        return "Task created successfully"
    return "Something went wrong"


def delete(id):
    """
    Deletes a task by its ID.
    """
    if not isinstance(id, int) or id <= 0:
        return "Invalid ID. Please provide a positive integer."
    
    if delete_work(id):
        return f"Task {id} deleted successfully."
    return f"Task with ID {id} not found."


def mark_done(id):
    """
    Marks a task as done by its ID.
    """
    if not isinstance(id, int) or id <= 0:
        return "Invalid ID. Please provide a positive integer."
    
    if mark_done(id):
        return f"Task {id} marked as done."
    return f"Task with ID {id} not found."


def mark_in_progress(id):
    """
    Marks a task as in progress by its ID.
    """
    if not isinstance(id, int) or id <= 0:
        return "Invalid ID. Please provide a positive integer."
    
    if mark_in_progress(id):
        return f"Task {id} marked as in progress."
    return f"Task with ID {id} not found."


def list(condition="all"):
    """
    Lists tasks based on the specified condition.
    """
    condition = condition.lower()
    if condition == "all":
        list_all()
    elif condition == "done":
        list_all_done()
    elif condition == "todo":
        list_all_todo()
    elif condition == "in_progress":
        list_all_in_progress()
    else:
        return "Invalid condition. Use 'all', 'done', or 'in_progress'."


def update(id, new_title):
    """
    update the task with given id 
    """
    update_work(id, new_title)

if __name__ == "__main__":
    fire.Fire()
