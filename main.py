import storage
import ui
import action
import constants
import time

data = storage.load_data()
while True:
    ui.list_menu(data)
    section = input("Enter the section title: ")
    
    if section in constants.STOP_COMMANDS:
        action.stop()
        break
    
    elif section in constants.ADD_COMMANDS:
        ui.list_menu(data)
        name = input("Name of the New Section: ")
        if name in constants.STOP_COMMANDS:
            action.stop()
            continue
        else:
            action.add_section(data, name)
            storage.save_data(data)
    
    elif section in constants.DEL_COMMANDS:
        ui.list_menu(data)
        name = input("Name of the section to be deleted: ")
        if name in constants.STOP_COMMANDS:
            action.stop()
            continue
        elif name in data["sections"]:
            ui.list_menu(data)

            confirm = input("Are you sure you want to delete an entire section? (y/n): ")
            if confirm == "n":
                    continue
            elif confirm == "y":
                    captcha = action.get_captcha()
                    ui.list_menu(data)
                    print(f"CAPTCHA - {captcha}")
                    user_input = input("Enter the CAPTCHA to confirm. - ")
                    if user_input == captcha:
                        action.delete_section(data, name)
                        storage.save_data(data)
                    else:
                        continue
    elif section in data["sections"]:
         while True:
              ui.list_tasks_menu(data, section)
              command = input("Select a task: ")
              if command in constants.STOP_COMMANDS:
                   action.stop()
                   break
              
              elif command in constants.ADD_COMMANDS:
                   ui.list_tasks_menu(data, section)
                   new_task_name = input("Enter the name of the new task.: ")
                   if new_task_name in constants.STOP_COMMANDS:
                        action.stop()
                        break
                   else:
                        action.add_task(data, section, new_task_name)
                        storage.save_data(data)
              
              elif command in constants.DEL_COMMANDS:
                   ui.list_tasks_menu(data, section)
                   task_to_delete = input("Enter the name of the task to be deleted: ")
                   if task_to_delete in constants.STOP_COMMANDS:
                        action.stop()
                        continue
                   elif task_to_delete in data["sections"][section]["tasks"]:
                        action.delete_task(data, section, task_to_delete)
                        storage.save_data(data)
              
              elif command in constants.DONE_COMMANDS:
                   ui.list_tasks_menu(data, section)
                   task_to_done = input("Select a task: ")
                   if task_to_done in data["sections"][section]["tasks"]:
                        action.mark_task_done(data, section, task_to_done)
                        storage.save_data(data)
              
              elif command in data["sections"][section]["tasks"]:
                start_time = time.time()
                try:
                    while True:
                        current_session = time.time() - start_time
                        total_time = data["sections"][section]["tasks"][command]["time"] + current_session
                        formatted_time = time.strftime('%H:%M:%S', time.gmtime(total_time))
            
                        ui.show_timer(data, section, command, formatted_time)
                        time.sleep(1)
    
                except KeyboardInterrupt:
                        
                        action.add_time_to_task(data, section, command, current_session)
                        storage.save_data(data)
                        print("Stopped")
                   

