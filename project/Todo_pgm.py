tasks={}
id=1

def add_task():
    global tasks
    global id
    tasks[id] = {"task": task_name, "status": False}
    id+=1

def update_task():
    task_id=int(input("enter the id to update"))
        

def show_task():
    if not tasks:
        print("no task available")
    else:
        print("Tasks")
        for k in tasks:
           print(f"{k} {tasks[k]['task']} - ","Done" if tasks[k]['status'] else "Incomplete")
def remove_task():
    pass
while True:
    print("Todo Task")
    print("1.add task\n2.update task\n3.show task\n4.remove task")
    c=int(input("enter your choice :"))
    if c==1:
        task_count=int(input("enter the count you want to add : "))
        for i in range(task_count):
            task_name=input("enter new tasks : ")
            print("task added")
            add_task()
    if c==3:
        show_task()
            
        