import datetime

def log_message(type, extension):
    with open("message_log.txt", "a") as log_file:
        if type == "extension":
            log_file.write(f"{datetime.datetime.now()}: Directory present for file extension {extension}\n")
        elif type == "file":
            log_file.write(f"{datetime.datetime.now()}: Moved file to directory with {extension}\n")