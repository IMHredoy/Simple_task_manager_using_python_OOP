from datetime import datetime
from uuid import uuid4

class Task:
    def __init__(self, task: str) -> None:
        self.id = uuid4()
        self.task = task
        self.created_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.updated_time = 'NA'
        self.completed = False
        self.completed_time = 'NA'
    
    def update_task(self, new_task:str) -> None:
        self.task = new_task
        self.updated_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        print("Task Updated Successfully\n")
    
    def complete_task(self) -> None:
        self.completed = True
        self.completed_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        print("Task Completed Successfully\n")

class Task_Manager:
    def __init__(self) -> None:
        self.all_tasks = []
        self.incompleted_task = []
        self.completed_tasks = []

    def add_new_task(self, task: Task) -> None:
        self.all_tasks.append(task)
        self.incompleted_task.append(task)
        print("Task Created Successfully\n")
    
    def display_task(self, task: Task) -> None:
        print(f"ID - {task.id}")
        print(f"Task - {task.task}")
        print(f"Created time - {task.created_time}")
        print(f"Updated time - {task.updated_time}")
        print(f"Completed - {task.completed}")
        print(f"Completed time - {task.completed_time}")
        print()

    def show_all_tasks(self) -> list:
        if len (self.all_tasks) == 0:
            print("There Is No Task In The List\n")
        else:
            return self.all_tasks
    
    def show_incompleted_tasks(self) -> list:
        if len (self.incompleted_task) == 0:
            print("No Incompleted Task\n")
        else:
            return self.incompleted_task
        
    def show_completed_tasks(self) -> list:
        if len (self.completed_tasks) == 0:
            print("No Completed Task\n")
        else:
            return self.completed_tasks