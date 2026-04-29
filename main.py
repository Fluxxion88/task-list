import storage
import ui
import action
import constants

while True:
    data = storage.load_data()
    ui.list_menu(data)
    section = input("Enter the section title: ")
    
    if section in constants.STOP_COMMANDS:
        action.stop()
        break
    
    elif section == "add":
        ui.list_menu(data)
        name = input("Name of the New Section: ")
        if name in constants.STOP_COMMANDS:
            action.stop()
            continue
        else:
            storage.add_section(data, name)
            storage.save_data(data)
    
    elif section == "del":
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
                        del data["sections"][name]
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
              elif command == "add":
                   ui.list_tasks_menu(data, section)
                   new_task_name = input("Enter the name of the new task.: ")
                   if new_task_name in constants.STOP_COMMANDS:
                        action.stop()
                        break
                   else:
                        