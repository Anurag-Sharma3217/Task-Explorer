import Utils as ut, requests

def menu():
    print('''===== TASK EXPLORER =====
1. View tasks by userID
2. View completed tasks
3. View tasks by task title
4. View task details by ID
5. Search task titles
6. Exit
Choose an option:''')
    choice = ut.get_number("What you want to do? ", "Enter s.no only.")
    return choice

def fetch_task(params=None):
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

def view_tasks():
    try:
        while True:
            userId = ut.get_number("Enter userID (1-10): ", "Enter number only.")
            if 0 <= userId <= 10:
                tasks = fetch_task({"userId": userId})
                for task in tasks:
                    print("Task's ID:", task["id"])
                    print("Task's title:", task["title"])
                    if task["completed"]:
                        print("Task's status: Completed\n")
                    else:
                        print("task's status: Incompleted\n")
                return
            
            else:
                print("Entry range: 1-10")

    except requests.RequestException as error:
        print(f"Request failed {error}")

def view_completed_tasks():
    try:
        while True:
            userId = ut.get_number("Enter userID (1-10): ", "Enter number only.")  
            if 1 <= userId <= 10:
                tasks = fetch_task({"userId": userId})
                for task in tasks:
                    if task["completed"]:
                        print("Task's status: Completed") 
                        print("Task's title: ", task["title"])
                        print("Task's ID: ", task["id"])
                return
            
            else:
                print("Entry range: 1-10")

    except requests.RequestException as error:
        print(f"Request failed {error}")

def search_status():
    try:
        while True:
            tasks = fetch_task()
            title = ut.get_name("Enter task's title: ")
            for task in tasks:
                if title.lower() == task["title"].lower():
                    print("Task's ID", task["id"])
                    print("Task's title", task["title"])
                    if task["completed"]:
                        print("Task's status: Completed\n")
                    else:
                        print("task's status: Incompleted\n")
                    return
                
            else:
                print("Title not found.")

    except requests.RequestException as error:
        print(f"Request failed {error}")

def view_task_id():
    try:
        while True:
            tasks = fetch_task()
            task_id = ut.get_number("Enter task's ID (1-200): ", "Enter number only.")
            if 1 <= task_id <= 200:
                for task in tasks:
                    if task_id == task["id"]:
                        print("Task's id:", task["id"])
                        print("Task's title:", task["title"])
                        if task["completed"]:
                            print("Task's status: Completed\n")
                        else:
                            print("task's status: Incompleted\n")
                        return
                
                else:
                    print("Task not found.")
                    return

            else:
                print("Entry range: 1-200")

    except requests.RequestException as error:
        print(f"Request failed {error}")

def search_title():
    try:
        while True:
            tasks = fetch_task()
            keyword = ut.get_name("Enter task's title: ")
            found = False
            for task in tasks:
                if keyword.lower() in task["title"].lower():
                    found = True
                    print(task["id"], task["title"])

            if found == False:
                print("Task not found.")

            return

    except requests.RequestException as error:
        print(f"Request failed: {error}")

def exit_program():
    print("Thank you for using this application.")

def invalid():
    print("Invalid option.")