import os
from organize_files import organize_files

def main():
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Files")
    organize_files(base_dir)
if __name__ == "__main__":
    main()