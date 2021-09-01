tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# # Print a list of uncompleted tasks
def uncompleted(list):
    task_uncompleted = []
    for task in list:
        if task["completed"] == False:
            task_uncompleted.append(task["description"])
    print(task_uncompleted)        
# uncompleted(tasks)

# # Print a list of completed tasks
def completed(list):
    task_completed = []
    for task in list:
        if task["completed"] == True:
            task_completed.append(task["description"])
    print(task_completed)
# completed(tasks)        

# # Print a list of all task descriptions

def task_decription(list):
    task_described = []
    for task in list:
        task_described.append(task["description"])
    print(task_described)
# task_decription(tasks)    

# # Print a list of tasks where time_taken is at least a given time
def time_for_task(list, given_time):
    tasks_with_time = []
    for task in list:
        if int(given_time) > task["time_taken"]:
            tasks_with_time.append(task["description"])
    print(tasks_with_time)
# time_for_task(tasks, 20) # Middle time to show some
# time_for_task(tasks, 1) # Beginning time to show all
# time_for_task(tasks,100) # End time to show none

# # Print any task with a given description
def described_task(list, given_description):
    for task in list:
        if given_description == task["description"]:
            print(task)
# described_task(tasks, 'Wash Dishes') # First task
# described_task(tasks, 'Walk Dog') # Last task

# # Given a description update that task to mark it as complete.
# def update_task(list, completed_task):
#     for task in list:
#         if completed_task == task["description"]:
#             task["completed"] = True
#     print(tasks)
# update_task(tasks, 'Clean Windows')        

# # Add a task to the list
def add_task(list, task_name, task_status, task_time):
    list.append({
        "description": task_name,
        "completed": task_status,
        "time_taken": task_time
    })
#     print(tasks)
# # add_task(tasks, "Hoover", True, 20)

# add_task(tasks, input("What task is it? "), input("What is the status of the task? "), input("How long will the task take? "))
def print_all():
    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")

menu = True
while menu == True:
    print_all()
    key_input = input("Please press a key").lower()
    if key_input == str(1):
        print(tasks)
    elif key_input == str(2):
        uncompleted(tasks)
    elif key_input == str(3):
        completed(tasks)   
    elif key_input == str(4):
        task_decription(tasks)    
    elif key_input == str(5):
        time_for_task(tasks, input("Please enter a time"))
    elif key_input == str(6):
        described_task(tasks, input("Please enter a task"))
    elif key_input == str(7):
        add_task(tasks, input("What task is it? "), input("What is the status of the task? "), input("How long will the task take? "))
    elif key_input == "m":
        print_all()
    elif key_input == "q":
        break    
    else:
        print("That key was not recognised")