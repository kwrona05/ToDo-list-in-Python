def ToDo_List():
    ToDo = []

    while True:
        print('\n1. Add task')
        print('2. Remove task')
        print('3. Show list')
        print('4. Finish')

        choice = input('choose an option (1/2/3/4): ')

        if choice == '1':
            task = input('Enter the task')
            ToDo.append(task)
            print(f'Add {task} to list')
        elif choice == '2':
            task = input('Enter name of the task')
            if task in ToDo:
                ToDo.remove(task)
                print(f'{task} removed')
            else:
                print("Task isn't on the list")
        elif choice == '3':
            print('Your ToDo list: ')
            for item in ToDo:
                print(f'- {item}')
        elif choice == '4':
            print('End of the program')
            break
        else:
            print('Choose the correct option')
ToDo_List()