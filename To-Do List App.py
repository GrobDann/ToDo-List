ToDo = True
tasks = [ ]
while ToDo == True:
    Mode = int(input('User press\n1 Add Task\n2 View tasks\n3 Remove task\n4 Quit\n> '))
    if Mode == 4:
        ToDo = False

    elif Mode == 3:
        remove_num = int(input('What task do you want removed?\n>'))
        tasks.pop(remove_num - 1)
    
    elif Mode == 2:
            for i, task in enumerate(tasks, start=1):
                 print('>>', i, task)
    
    elif Mode == 1:
        task = input('Enter in a task\n> ')
        tasks.append(task)

    if len(tasks) == 0:
         print("No tasks yet.")