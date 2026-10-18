import Function

choice = 0
while choice != 5:

    choice = Function.menu()

    if choice == 1:
        Function.view_tasks()

    elif choice == 2:
        Function.view_completed_tasks()

    elif choice == 3:
        Function.search_title()

    elif choice == 4:
        Function.view_task_id()

    elif choice == 5:
        Function.search_title()

    elif choice == 6:
        Function.exit_program()

    else:
        Function.invalid()