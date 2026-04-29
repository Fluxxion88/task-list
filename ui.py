import os

def list_razdel(data):                                              #ui
    for count, name in enumerate(data["sections"], 1):
        print(f"{count}. {name}")


def list_tasks(razdel_name):                                    #ui
    for count, name in enumerate(data["sections"][razdel_name]["tasks"], 1):
        task_status = data["sections"][razdel_name]["tasks"][name]["status"]
        if task_status == STATUS_DONE:
            print(f"{count}. {name} ✓")
        else:
            print(f"{count}. {name}")

def list_menu(data):
    os.system('clear')
    print("---Select a section---")
    list_razdel(data)

def list_tasks_menu(data, section_name):
    
