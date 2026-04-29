import storage
import ui
import action


STATUS_NOT_STARTED = "not started"
STATUS_DONE = "done"

while True:
    data = storage.load_data()
    ui.list_menu(data)
    section = input("Enter the section title: ")
    
    if section in ["stop", "Stop"]:
        action.stop()
        break
    
    elif section == "add":
        ui.list_menu(data)
        name = input("Name of the New Section: ")
        if name in ["stop", "Stop"]:
            action.stop()
            continue
        else:
            storage.add_section(data, name)
            storage.save_data(data)
    
    elif section == "del":
        ui.list_menu(data)
        name = input("Name of the section to be deleted: ")
        if name in ["stop", "Stop"]:
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
              ui.list
