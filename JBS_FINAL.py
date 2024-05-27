Id = 0
no_of_task = 0

class Task:
    def __init__(self, Id, title, description, priority, status):
        self.Id = Id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
    def __str__(self):
        return f"Task Id: {self.Id}, Title: {self.title}, Description: {self.description}, Priority: {self.priority}, Status: {self.status}"


class TaskManager:
    def __init__(self):
        self.d = []
    def add_task(self):
        global Id, no_of_task
        Id += 1
        tit = input("Enter task title:")
        des = input("Enter task description:")
        while True:
            pri = input("Enter task priority (High/Medium/Low):")
            if pri in ['High', 'Medium', 'Low']:
                break
            else:
                print("Invalid entry. Please try again.")
        while True:
            sta = input("Enter task status (Pending/In Progress/Completed):")
            if sta in ['Pending', 'In Progress', 'Completed']:
                break
            else:
                print("Invalid entry. Please try again.")
        task = Task(Id, tit, des, pri, sta)
        self.d.append(task)
        no_of_task += 1
    def edit_task(self, task_id):
        for task in self.d:
            if task.Id == task_id:
                task.title = input("Enter new task title:")
                task.description = input("Enter new task description:")
                while True:
                    task.priority = input("Enter new task priority (High/Medium/Low):")
                    if task.priority in ['High', 'Medium', 'Low']:
                        break
                    else:
                        print("Invalid entry. Please try again.")
                while True:
                    task.status = input("Enter new task status (Pending/In Progress/Completed):")
                    if task.status in ['Pending', 'In Progress', 'Completed']:
                        break
                    else:
                        print("Invalid entry. Please try again.")
                break
        else:
            print("Task not found")
    def delete_task(self, task_id):
        for i, task in enumerate(self.d):
            if task.Id == task_id:
                self.d.pop(i)
                break
    def get_task_by_id(self, task_id):
        for task in self.d:
            if task.Id == task_id:
                return task
    def view_all_tasks(self):
        for task in self.d:
            print(task)
    def filter_tasks_by_priority(self, priority):
        for task in self.d:
            if task.priority == priority:
                print(task)
            


def choice():
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. View all Task")
    print("5. Filter Tasks by Priority")
    print("6. Exit")


task_manager = TaskManager()

while True:
    choice()
    i = input("Enter your choice (1-6): ")
    if i == '6':
        print("Exit")
        break
    elif i == '1':
        print("**********Add_task**********")
        task_manager.add_task()
    elif i == '2':
        print("***********Edit_task*****************")
        while True:
            et = input("Enter task ID to edit:")
            if et.isdigit() and int(et) <= no_of_task:
                et = int(et)
                break
            else:
                print("Invalid entry. Please try again.")
        task_manager.edit_task(et)
    elif i == '3':
        print("*************delete_task**************")
        while True:
            de = input("Enter task ID to delete:")
            if de.isdigit() and int(de) <= no_of_task:
                de = int(de)
                break
            else:
                print("Invalid entry. Please try again.")
        task_manager.delete_task(de)
    elif i == '4':
        print("****************view_all_task************")
        task_manager.view_all_tasks()
    elif i == '5':
        print("****************filter task by priority************")
        while True:
            p = input("Enter the priority to filter tasks (High/Medium/Low) : ")
            if p in ['High', 'Medium', 'Low']:
                break
            else:
                print("Invalid entry. Please try again.")
        task_manager.filter_tasks_by_priority(p)
    else:
        print("Invalid entry.Please try again")
        choice()