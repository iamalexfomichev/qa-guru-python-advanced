
import json
import os

def load_user_data():
    file_path = os.path.join(os.path.dirname(__file__), "user_list.json")
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
