# ACIT4420-FileOrganizer

This program is created as a part of the course ACIT4420. **ACIT4220-FileOrganizer** is a tool created to orgnaize and sort files based on their extension, and adds new extension folders if needed.The package includes four python files: **config.py**, **organize_files.py**, **sort_files.py** and **logger.py**. Additonaly the program has a `__main__.py` entrypoint, an `__init__.py` file to mark it as module, and a **log_message.txt** file for logging.

## Table of Contents
- [Features](#features)
- [Installation Manual](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Key Files](#key-files)
- [License](#license)
  
## Features
- Sort existing files into corresponding extension folders.
- Dynamically creates extension folder if needed.
- Print the changes executed.
- Modular design for easy extension and maintenance.
  
## Installation Manual

Follow these simple steps to install and set up the project:

1. **Clone the Repository**

Firstly, clone the repository from GitHub (or download the package manually):

```bash
git clone https://github.com/bowcarl/ACIT4420-FileOrganizer.git
cd ACIT4420-FileOrganizer
```
2. **Create a virtual environment**

Furthermore, It's recommended to create a virtual environment to isolate the project dependencies. Continue and run the following commands:

```bash
python3 -m venv organizergenv
source organzierenv/bin/activate # or with windows use `organizerenv\Scripts\activate`
```

3. **Install the Package**

With your virtual environment set up, install the project using the pip tool:

```bash
pip install -e .
```

## Usage
Once the package is installed you only need to run this command in your preffered terminal:
```bash
FileOrganizer
```
This will try to look for files in the File folder, and start sorting and if needed create new subfolders for specific extension names. For each action, you will recieve a message, stateing what happend.

## Project Structure
```
ACIT4420-FileOrganizer/
│
├── FileOrganizer/
|   ├── __pyache__.py
|       ├── (...).py
|   ├── Files
|       ├── (...).{extension}
│   ├── __init__.py
│   ├── __main__.py                # Entry point for the module
│   ├── config.py
│   ├── logger.py
|   ├── message_log.txt
|   ├── organize_files.py
│   └── sort_files.py
│
├── setup.py                   # Installation script
└── README.md                  # Project documentation (this file)
```
### Key Files
- **`__main__.py`**: Contains the main function that launces the option menu.
- **`setup.py`**: Scripts for installing the package.
- **`config.py`**: Creates new extension folders
- **`logger.py`**: Loggs all current directories and all moves executed 
- **`organize_files.py`**: Prepares for sorting and adding extension folders
- **`sort_files.py`**: Sort files based on their extension name, and create extension files if needed

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/shailendrabhandari/project_game/blob/main/LICENSE) file for details.

