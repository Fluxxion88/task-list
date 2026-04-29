import json
from constants import STATUS_DONE, STATUS_NOT_STARTED

def save_data(data):
    with open("profile.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def add_section(data, name):
    data["sections"][name] = {"tasks":{}}
    with open("profile.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
def load_data():
    with open("profile.json", 'r', encoding='utf-8') as file:
        return json.load(file)

def add_task(data, section, new_task_name):
    data["sections"][section]["tasks"][new_task_name] = {
                    "time": 0,
                    "status": STATUS_NOT_STARTED
                }
    