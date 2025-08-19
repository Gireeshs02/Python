def add_task(tasks, task):
    """
    This function adds a new task to the list of tasks.

    Args:
        tasks (list): The list of tasks.
        task (str): The task to be added.

    Returns:
        None
    """
    tasks.append(task)


def remove_task(tasks, task):
    """
    This function removes a specified task from the list of tasks.

    Args:
        tasks (list): The list of tasks.
        task (str): The task to be removed.

    Returns:
        None
    """
    tasks.remove(task)


def display_tasks(tasks):
    """
    This function displays all the tasks in the list of tasks.

    Args:
        tasks (list): The list of tasks.

    Returns:
        None
    """
    print("Tasks:")
    for task in tasks:
        print(task)


def main():
    """
    This is the entry point of the program. It displays a menu of options to the user and performs the corresponding action based on the user's choice.

    Args:
        None

    Returns:
        None
    """
    tasks = []
    while True:
        print("Enter 1 to add a task")
        print("Enter 2 to display tasks")
        print("Enter 3 to remove a task")
        print("Enter 4 to quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == 2:
            display_tasks(tasks)
        elif choice == 3:
            task = input("Enter the task to remove: ")
            remove_task(tasks, task)
        elif choice == 4:
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
