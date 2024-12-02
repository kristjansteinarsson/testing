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

def save_user(file_name, data):
    """Save data to a JSON file."""
    file_path = os.path.join("storage", file_name)
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error: Failed to save data to {file_name}: {e}")

def clear_screen(self):
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')