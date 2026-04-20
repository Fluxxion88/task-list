import json


data = {
    "sections": [
        {
            "name": "NeetCode",
            "tasks": [
                {"name": "twosum", "time": 0, "Status": "not started"},
                {"name": "valid anagram", "time": 0, "Status": "not started"}
            ]
        }
    ]
}
with open("profile.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

