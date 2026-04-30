import os
import random
import string
from constants import STATUS_DONE, STATUS_NOT_STARTED

def stop():                                                     #actions
    os.system('clear')
    print("See you soon!")
    
def get_captcha():                                              #actions
    pool = string.ascii_lowercase + string.digits
    random_chars = random.choices(pool, k=4)
    return "".join(random_chars)

def add_time_to_task(data, section, task_name, seconds):
    data["sections"][section]["tasks"][task_name]["time"] += seconds


def add_section(data, name):
    data["sections"][name] = {"tasks":{}}
    with open("profile.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def add_task(data, section, new_task_name):
    data["sections"][section]["tasks"][new_task_name] = {
                    "time": 0,
                    "status": STATUS_NOT_STARTED
                }

def delete_section(data, name):
    del data["sections"][name]

def delete_task(data, section, task_name):
    del data["sections"][section]["tasks"][task_name]

def mark_task_done(data, section, task_name):
    data["sections"][section]["tasks"][task_name]["status"] = STATUS_DONE
