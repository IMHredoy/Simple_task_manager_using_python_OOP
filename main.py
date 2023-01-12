from task_manager import *

TM = Task_Manager()

while True:
    print("0. Choose this quit")
    print("1. Add New Task")
    print("2. Show All Task")
    print("3. Show Incomplete Tasks")
    print("4. Show Completed Tasks")
    print("5. Update Task")
    print("6. Mark A Task Completed")

    option = input("Enter Option: ")
    match option:
        case '0':
            break
        case '1':
            task_name = input("Enter New Task: ")
            print()
            t = Task(task_name)
            TM.add_new_task(t)
        case '2':
            print()
            tasks_list = TM.show_all_tasks()
            if tasks_list:
                for task in tasks_list:
                    TM.display_task(task)            
        case '3':
            print()
            tasks_list = TM.show_incompleted_tasks()
            if tasks_list:
                for task in tasks_list:
                    TM.display_task(task)
        case '4':
            print()
            tasks_list = TM.show_completed_tasks()
            if tasks_list:
                for task in tasks_list:
                    TM.display_task(task)
        case '5':
            print()
            print("Select Which Task To Update\n")
            tasks_list = TM.show_all_tasks()

            if tasks_list:
                for no, task in enumerate(tasks_list, start=1):
                    print(f"Task No - {no}")
                    TM.display_task(task)

                task_no = int(input("Enter Task No: "))
                if task_no <= len(tasks_list) and task_no >= 1:
                    new_task = input("Enter New Task: ")
                    print()

                    tasks_list[task_no-1].update_task(new_task)
                else:
                    print("\nInvalid Task No\n")
        case '6':
            print()
            print("Select Which Task To Complete\n")
            tasks_list = TM.show_incompleted_tasks()
            if tasks_list:
                for no, task in enumerate(tasks_list, start=1):
                    print(f"Task No - {no}")
                    TM.display_task(task)
                    
            task_no = int(input("Enter Task No: "))
            if task_no <= len(tasks_list) and task_no >= 1:    
                
                print()
                tasks_list[task_no-1].complete_task()
                TM.completed_tasks.append( TM.incompleted_task.pop(task_no - 1))
            else:
                print("\nInvalid Task No\n")
        case _:
            print("\nInvalid Option\n")