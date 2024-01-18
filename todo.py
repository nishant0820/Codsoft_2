import os

def load_task_from_file(file_path):
    task=[]
    if os.path.exists(file_path):
        with open(file_path,"r") as file:
            task=file.read().splitlines()
    return task

def save_task(file_path,task):
    with open(file_path,"w") as file:
        for task in task:
            file.write(f"{task}\n")
            
def show_task(task):
    if not task:
        print("No Tasks Found.")
    else:
        for i,task in enumerate(task,1):
            print(f"{i}.{task}")
            
def add_task(task,new_task):
    task.append(new_task)
    print("Task Added Successfully.")
    
def update_task(task,index,updated):
    if 1<=index<=len(task):
        task[index-1]=updated
        print("Task Updated Successfully.")
    else:
        print("Invalid Task Index.")
        
def delete_task(task,index):
    if 1<=index<=len(task):
        delete_task=task.pop(index-1)
        print(f"Task Deleted Successfully.")
    else:
        print("Invalid Task Index.")

def main():
    file_path="todo.txt"
    task=load_task_from_file(file_path)
    while True:
        print("\n=============== Todo List ================")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Show Task")
        print("5. Save & Exit")
   
        choice=input("Enter your choice (1-5): ")
        if(choice=="4"):
            show_task(task)
        elif(choice=="1"):
            new_task=input("Enter the task to add: ")
            add_task(task,new_task)
        elif(choice=="2"):
            index=int(input("Enter the task index to update: "))
            updated=input("Enter the updated task: ")
            update_task(task,index,updated)
        elif(choice=="3"):
            index=int(input("Enter the task index to delete: "))
            delete_task(task,index)
        elif(choice=="5"):
            save_task(file_path,task)
            print("Task Saved. Exiting...")
            break
        else:
            print("Invalid Choice. Please try again.")
    
if __name__=="__main__":
    main()