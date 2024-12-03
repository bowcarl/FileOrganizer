import os
import sys

# Ensure the parent directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(file), '../../')))
sys.path.insert(0, os.path.abspath(os.path.dirname(file)))
from organize_files import organize_files

def main():
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Files")
    organize_files(base_dir)
if __name__ == "__main__":
    main()
