import json
import argparse

with open("profile.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

def add_class(som):
    data["sections"].append({"name": som, "tasks": []})
    
    with open("profile.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        print("Новый раздел добавлен!! ")

parser = argparse.ArgumentParser()

parser.add_argument("action")
parser.add_argument("value", nargs='?', default=None)

args = parser.parse_args()

if args.action == "add_class":
    add_class(args.value)
elif args.action == "list":
    x = 1
    for i in data["sections"]:
        print(f"{x}. {i["name"]}")
        x += 1



else:
    print("Ты чё упоротый?! ты же сам писал этот код, как блять ошибся олух")

