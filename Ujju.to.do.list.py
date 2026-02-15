

def todo_app():
    tasks = []
    
    while True:
        print("\n--- Ujjwal. To-Do List ---")
        print("1. Add Task ")
        print("2. Show Tasks ")
        print("3. Delete Task ")
        print("4. Exit ")
        
        choice = input("\n select your options (1-4): ")
        
        if choice == '1':
            new_task = input("Write the name of task : ")
            tasks.append(new_task)
            print("OK, ADD")
            
        elif choice == '2':
            if not tasks:
                print("The list is still empty")
            else:
                print("\nYour list :")
                for index, item in enumerate(tasks, 1):
                    print(f"{index}. {item}")
                    
        elif choice == '3':
            if not tasks:
                print("There is nothing to remove:")
            else:
                try:
                    num = int(input("Which Number to delete: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print(f"'{removed}' Removed")
                    else:
                        print("Oho, Enter the correct numbber:")
                except ValueError:
                    print("Please enter only the number(1, 2, 3, 4)")
                    
        elif choice == '4':
            print("Ok friends see you again ")
            break
        else:
            print("Wrong button pressed, Try again :")

# Running for programe  
if __name__ == "__main__":
    todo_app()
