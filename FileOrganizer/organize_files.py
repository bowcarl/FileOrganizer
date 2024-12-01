import os
from sort_files import file_sorter
from config import CONFIG, add_extension
import re
from logger import log_message

def organize_files(base_dir):
    try:
        # Handle non-existent base directory
        if not os.path.exists(base_dir):
            raise FileNotFoundError(f"The base directory '{base_dir}' does not exist.")
        
        # Check for read permissions on the base directory
        if not os.access(base_dir, os.R_OK):
            raise PermissionError(f"Read permission denied for base directory: {base_dir}")
        
        # Traverse through files in the base_dir and process them
        for file_name in os.listdir(base_dir):
            # Skip directories and ensure it's a valid file
            file_pattern = re.compile(r"^.+\.[a-zA-Z0-9]+$")
            if file_pattern.match(file_name):
                file_extension = os.path.splitext(file_name)[1].lower()

                if file_extension not in CONFIG:
                    add_extension(file_extension, [file_extension], file_extension[1:].upper())  # Add new category
                    log_message("extension", file_extension)
                file_sorter(file_name, base_dir)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except Exception as e:
        raise Exception(f"Failed to organize files: {e}")
