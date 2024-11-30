import json
import os

def load_json_data(file_name):
    """Load and return data from a JSON file."""
    file_path = os.path.join("storage", file_name)
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_name}.")
        return []