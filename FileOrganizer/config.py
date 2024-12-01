CONFIG={}

def add_extension(file_type, extensions, folder):
    "Add dynamic extension direcotry"
    CONFIG[file_type] = {
        "extensions": extensions,
        "folder": folder
    }
    
