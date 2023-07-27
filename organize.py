import os
from tkinter import filedialog

print("\nWelcome to File Organizer, Please select the folder to organize")

#path of the folder which needs to be organized
folderpath = filedialog.askdirectory()

#if the folder is selected then go to that path else exit
if folderpath != "":
    os.chdir(folderpath)
else:
    exit()

for i in os.listdir():
    text_touple = os.path.splitext(i)
    extension = text_touple[-1]

    if extension != "":
        extension = extension.replace(".", "")

        try:
            os.mkdir(f"{extension}_Files")
        except FileExistsError:
            pass
        except Exception as e:
            print(e)

        try:
            os.replace(i, f"{extension}_Files/{i}")
        except Exception as e:
            print(f"Error in replacing file {i}: {e}")

    else:
        pass

print("File Organization Complete")
