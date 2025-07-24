def task_manager():
    task=[]
    print("_____________________WELCOME TO TASK MANAGEMENT APP_________________")
    total_tasks=int(input("Enter the numbers of tasks you want to add in the TO-Do list : "))
    for i in range(1,total_tasks+1):
        task_names=input(f"Enter task {i} : ")
        task.append(task_names)
    for item in task:
        print("Task you have to perform today are--- ",item)
    while True:
        print("""PRESS 1 if you want to add task
PRESS 2 if you want to update task
PRESS 3 if you want to remove task
PRESS 4 if you want to view the task list
PRESS 5 if you want to exit """)
        operation=int(input("Enter your choice : "))
        
        if operation==1:
            task_add=input("Enter the task you want to add : ")
            task.append(task_add)
            print("_____")
            print(f"Task {task_add} has been successfully added.")
            print("_____")

        elif operation==2:
            update_task=input("Enter the task you want to update = ")
            
            if update_task in task:
                updated=input("Enter the new task : ")
                place=task.index(update_task)
                task[place]=updated
                print("______")
                print("Task updated successfully")
                print(f"Updated task {updated}")
                print("______")
            
            
            else:
                print("____")
            
                print("OOPS! Task not found")
                print("____")
    
        elif operation==3:
            deleted_task=input("Enter the task which you want to delete : ")

            if deleted_task in task:
                place=task.index(deleted_task)
                del task[place]
                print("____")
            
                print(f"Task {deleted_task} has been deleted successfully")
                print("____")
            
            else:
                print("____")
                print(f"The task {deleted_task} does not exist in the list")
                print("_____")

        
        elif operation==4:
            for item in task:
                print("Tasks for the day are--> ",item)
            

        elif operation==5:
            print("THANK YOu!")
            break
        
        else:

            print("ENTER A VALID CHOICE!")

task_manager()