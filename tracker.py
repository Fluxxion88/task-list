import json
import os
import random
import string
import sys
import time 


with open("profile.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

def add_razdel(som):
    data["sections"][som] = {"tasks":{}}
    
    with open("profile.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

        print("New section added!! ")

def list_razdel():
    for count, name in enumerate(data["sections"], 1):
        print(f"{count}. {name}")


def list_tasks(razdel_name):
    for count, name in enumerate(data["sections"][razdel_name]["tasks"], 1):
        task_status = data["sections"][razdel]["tasks"][name]["status"]
        if task_status == "done":
            print(f"{count}. {name} ✓")
        else:
            print(f"{count}. {name}")

def stop():
    os.system('clear')
    print("See you soon!")

def save_data():
    with open("profile.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def get_captcha():
    pool = string.ascii_lowercase + string.digits
    random_chars = random.choices(pool, k=4)
    return "".join(random_chars)


while True:
    os.system('clear')
    print("---Select a section---")
    list_razdel()

    razdel = input("Enter the section title.: ")

    if razdel in ["stop", "Stop", "ыещз"]:
        stop()
        break

    elif razdel == "add":
        os.system('clear')
        print("---Select a section---")
        list_razdel()
        name = input("Name of the New Section: ")
        if name in ["stop", "Stop", "ыещз"]:
            stop()
            break
        add_razdel(name)
    
    elif razdel in ["del", "delete"]:
        os.system('clear')
        print("---Select a section---")
        list_razdel()
        name = input("Name of the section to be deleted: ")

        if name in data["sections"]:
            os.system('clear')
            print("---Select a section---")
            list_razdel()
            shure = input("Are you sure you want to delete an entire section? (y/n): ")
            if shure == "n":
                continue
            elif shure == "y":
                captcha = get_captcha()
                os.system('clear')
                print("---Select a section---")
                list_razdel()
                print(f"CAPTCHA - {captcha}")
                gg_razdelu = input("Enter the CAPTCHA to confirm. - ")
                if gg_razdelu == captcha:
                    del data["sections"][name]

    
    elif razdel in data["sections"]:
        os.system('clear')

        while True:
            os.system('clear')
            print(f"--- Section Objectives {razdel} ---")
            list_tasks(razdel)
                                                         
            gomer = input("Select a task: ")           

            if gomer in ["stop", "Stop", "ыещз", "back", "назад"]:
                stop()
                break

            elif gomer == "add":
                os.system('clear')
                print(f"--- Section Objectives {razdel} ---")
                list_tasks(razdel)
                new_task_name = input("Enter the name of the new task.: ")
                data["sections"][razdel]["tasks"][new_task_name] = {
                    "time": 0,
                    "status": "Not Started"
                }

                save_data()
                print(f"New Section {new_task_name} added!! ")

            elif gomer in ["del", "delete"]:
                os.system('clear')
                print(f"--- Section Objectives {razdel} ---")
                list_tasks(razdel)
                task_to_delete = input("Enter the name of the task to be deleted: ")
                
                if task_to_delete in data["sections"][razdel]["tasks"]:
                    del data["sections"][razdel]["tasks"][task_to_delete]
                    save_data()
            
            elif gomer in data["sections"][razdel]["tasks"]:
                start_time = time.time()
                try:
                    while True:
                        os.system('clear')
                        print(f"--- Section Objectives {razdel} ---")
                        cureent_session = time.time() - start_time
                        total_time = data["sections"][razdel]["tasks"][gomer]["time"] + cureent_session
                        formated_time = time.strftime('%H:%M:%S', time.gmtime(total_time))

                        for count, name in enumerate(data["sections"][razdel]["tasks"], 1):
                            task_status = data["sections"][razdel]["tasks"][name]["status"]
                            if name == gomer:
                                print(f"{count}. {name} - {formated_time}")
                            elif task_status == "done":
                                print(f"{count}. {name} ✓")
                            else:
                                print(f"{count}. {name}")
                        print("Press Ctrl + C to stop.")
                        time.sleep(1)
                
                except KeyboardInterrupt:
                    data["sections"][razdel]["tasks"][gomer]["time"] += cureent_session
                    save_data()
                    print("Stopped")

            elif gomer == "done" or gomer == "fin":
                os.system('clear')
                print(f"--- Section Objectives {razdel} ---")
                list_tasks(razdel)
                task_to_done = input("Select a task: ")
                if task_to_done in data["sections"][razdel]["tasks"]:
                    data["sections"][razdel]["tasks"][task_to_done]["status"] = "done"
                    save_data()


