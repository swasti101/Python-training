tasks = []  

def add_task(task):
    tasks.append({"task": task, "done": False})

def remove_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def mark_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

def show_tasks():
    for task in (tasks):
        status = "✓" if task["done"] else "✗"
        print(f"{task['task']} [{status}]")
    print("\n")


add_task("Study Python")
add_task("Complete Assignment")
show_tasks()
mark_complete(0)
show_tasks()
remove_task(1)
show_tasks()
