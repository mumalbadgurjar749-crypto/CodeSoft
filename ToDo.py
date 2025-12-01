def task():
    tasks = []
    print("----WELCOME TO THE TASK MANAGEMENT APP----")

    total_task = int(input("Enter how many task you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter Task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))

        # ADD OPERATION
        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")

        # UPDATE OPERATION
        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task {up}")   
            else:
                print("Task not found!")

        # DELETE OPERATION
        elif operation == 3:
            delete_val = input("Enter the task name you want to delete = ")
            if delete_val in tasks:
                tasks.remove(delete_val)
                print(f"Task {delete_val} deleted successfully.")
            else:
                print("Task not found!")

        # VIEW TASKS
        elif operation == 4:
            print(f"Your tasks: {tasks}")

        # EXIT
        elif operation == 5:
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid Input! Please choose 1–5.")
task()