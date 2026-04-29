import os
from constants import STATUS_DONE, STATUS_NOT_STARTED

def list_razdel(data):                                              #ui
    for count, name in enumerate(data["sections"], 1):
        print(f"{count}. {name}")


def list_tasks(data, section):                                    #ui
    for count, name in enumerate(data["sections"][section]["tasks"], 1):
        task_status = data["sections"][section]["tasks"][name]["status"]
        if task_status == STATUS_DONE:
            print(f"{count}. {name} ✓")
        else:
            print(f"{count}. {name}")

def list_menu(data):
    os.system('clear')
    print("---Select a section---")
    list_razdel(data)

def list_tasks_menu(data, section):
    os.system('clear')
    print(f"--- Section Objectives {section} ---")
    list_tasks(data, section)

