import json

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
    