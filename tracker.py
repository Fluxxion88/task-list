import json
import os
import random
import string
import sys
import time 

STATUS_NOT_STARTED = "not started"
STATUS_DONE = "done"

with open("profile.json", 'r', encoding='utf-8') as file:       #storage
    data = json.load(file)

def add_razdel(name):                                           #storage
    data["sections"][name] = {"tasks":{}}
    
    with open("profile.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

        print("New section added!! ")

def list_razdel():                                              #ui
    for count, name in enumerate(data["sections"], 1):
        print(f"{count}. {name}")


def list_tasks(razdel_name):                                    #ui
    for count, name in enumerate(data["sections"][razdel_name]["tasks"], 1):
        task_status = data["sections"][razdel_name]["tasks"][name]["status"]
        if task_status == STATUS_DONE:
            print(f"{count}. {name} ✓")
        else:
            print(f"{count}. {name}")

def stop():                                                     #actions
    os.system('clear')
    print("See you soon!")

def save_data():                                                #storage
    with open("profile.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def get_captcha():                                              #actions
    pool = string.ascii_lowercase + string.digits
    random_chars = random.choices(pool, k=4)
    return "".join(random_chars)


while True:
    os.system('clear')
    print("---Select a section---")
    list_razdel()

    section = input("Enter the section title.: ")

    if section in ["stop", "Stop", "ыещз"]:
        stop()
        break

    elif section == "add":
        os.system('clear')
        print("---Select a section---")
        list_razdel()
        name = input("Name of the New Section: ")
        if name in ["stop", "Stop", "ыещз"]:
            stop()
            continue
        add_razdel(name)
    
    elif section in ["del", "delete"]:
        os.system('clear')
        print("---Select a section---")
        list_razdel()
        name = input("Name of the section to be deleted: ")

        if name in data["sections"]:
            os.system('clear')
            print("---Select a section---")
            list_razdel()
            confirm = input("Are you sure you want to delete an entire section? (y/n): ")
            if confirm == "n":
                continue
            elif confirm == "y":
                captcha = get_captcha()
                os.system('clear')
                print("---Select a section---")
                list_razdel()
                print(f"CAPTCHA - {captcha}")
                user_input = input("Enter the CAPTCHA to confirm. - ")
                if user_input == captcha:
                    del data["sections"][name]
                    save_data()

    elif section in data["sections"]:
        os.system('clear')

        while True:
            os.system('clear')
            print(f"--- Section Objectives {section} ---")
            list_tasks(section)
                                                         
            command = input("Select a task: ")           

            if command in ["stop", "Stop"]:
                stop()
                sys.exit()
            elif command in ["back", "назад"]:
                os.system('clear')
                break

            elif command == "add":
                os.system('clear')
                print(f"--- Section Objectives {section} ---")
                list_tasks(section)
                new_task_name = input("Enter the name of the new task.: ")
                data["sections"][section]["tasks"][new_task_name] = {
                    "time": 0,
                    "status": STATUS_NOT_STARTED
                }

                save_data()
                print(f"New Section {new_task_name} added!! ")

            elif command in ["del", "delete"]:
                os.system('clear')
                print(f"--- Section Objectives {section} ---")
                list_tasks(section)
                task_to_delete = input("Enter the name of the task to be deleted: ")
                
                if task_to_delete in data["sections"][section]["tasks"]:
                    del data["sections"][section]["tasks"][task_to_delete]
                    save_data()

            elif command == STATUS_DONE or command == "fin":
                os.system('clear')
                print(f"--- Section Objectives {section} ---")
                list_tasks(section)
                task_to_done = input("Select a task: ")
                if task_to_done in data["sections"][section]["tasks"]:
                    data["sections"][section]["tasks"][task_to_done]["status"] = STATUS_DONE
                    save_data()

            
            elif command in data["sections"][section]["tasks"]:
                start_time = time.time()
                try:
                    while True:
                        os.system('clear')
                        print(f"--- Section Objectives {section} ---")
                        current_session = time.time() - start_time
                        total_time = data["sections"][section]["tasks"][command]["time"] + current_session
                        formatted_time = time.strftime('%H:%M:%S', time.gmtime(total_time))

                        for count, name in enumerate(data["sections"][section]["tasks"], 1):
                            task_status = data["sections"][section]["tasks"][name]["status"]
                            if name == command:
                                print(f"{count}. {name} - {formatted_time}")
                            elif task_status == STATUS_DONE:
                                print(f"{count}. {name} ✓")
                            else:
                                print(f"{count}. {name}")
                        print("Press Ctrl + C to stop.")
                        time.sleep(1)
                
                except KeyboardInterrupt:
                    data["sections"][section]["tasks"][command]["time"] += current_session
                    save_data()
                    print("Stopped")

            


