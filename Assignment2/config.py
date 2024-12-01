CONFIG={}

def add_extention(file_type, extensions, folder):
    "Add dynamic extention direcotry"
    CONFIG[file_type] = {
        "extensions": extensions,
        "folder": folder
    }
    