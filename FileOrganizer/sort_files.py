import os
import shutil
from config import CONFIG
from logger import log_message

def file_sorter(file_name, base_dir):
    # Get the file extension
    file_extension = os.path.splitext(file_name)[1].lower()

    try:
        # Checks if the file_extension exists in the CONFIG dictionary
        if file_extension in CONFIG:
            extension_data = CONFIG[file_extension]
            extension_path = os.path.join(base_dir, extension_data["folder"])

            # Create the folder if it doesn't exist
            if not os.path.exists(extension_path):
                os.makedirs(extension_path)
                print(f"Created a folder for the extension: {file_extension}")

            # Check for write permissions in the destination folder
            if not os.access(extension_path, os.W_OK):
                raise PermissionError(f"Write permission denied for directory: {extension_path}")

            # Move the file to the destination folder
            source_path = os.path.join(base_dir, file_name)
            target_path = os.path.join(extension_path, file_name)
            
            shutil.move(source_path, target_path)
            log_message("file", file_extension)
            print(f"Moved file {file_name} to {extension_path}")
        else:
            raise Exception(f"No extension found for file extension {file_extension}")

    except PermissionError as e:
        print(f"Error: {e}")
    except Exception as e:
        raise Exception(f"Failed to move file {file_name} to its extension: {e}")
