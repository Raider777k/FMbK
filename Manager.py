from tkinter import *
import shutil  # для обработки файлов, групп файлов, и папок
import os  # для работы с операционной системой
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb


def open_window():
    read = easygui.fileopenbox()
    return read

def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', "File not found!")

def copy_file():
    source1 = open_window()
    destination1 = filedialog.askdirectory()
    shutil.copy(source1, destination1)
    mb.showinfo('confirmation', "File Copied !")

def delete_file():
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)
    else:
        mb.showinfo('confirmation', "File not found !")

def rename_file():
    chosenFile = open_window()
    path1 = os.path.dirname(chosenFile)
    extension = os.path.splitext(chosenFile)[1]
    print("Enter new name for the chosen file")
    newName = input()
    path = os.path.join(path1, newName + extension)
    print(path)
    os.rename(chosenFile, path)
    mb.showinfo('confirmation', "File Renamed !")


def move_file():
    source = open_window()
    destination = filedialog.askdirectory()
    if source == destination:
        mb.showinfo('confirmation', "Source and destination are same")
    else:
        shutil.move(source, destination)
        mb.showinfo('confirmation', "File Moved !")

def make_folder():
    newFolderPath = filedialog.askdirectory()
    print("Enter name of new folder")
    newFolder = input()
    path = os.path.join(newFolderPath, newFolder)
    os.mkdir(path)
    mb.showinfo('confirmation', "Folder created !")

def remove_folder():
    delFolder = filedialog.askdirectory()
    os.rmdir(delFolder)
    mb.showinfo('confirmation', "Folder Deleted !")

def list_files():
    folderList = filedialog.askdirectory()
    sortlist = sorted(os.listdir(folderList))
    i = 0
    print("Files in ", folderList, "folder are:")
    while i < len(sortlist):
        print(sortlist[i] + '\n')
        i += 1

root = Tk()

canv = Canvas(root, width=400, height=20, bg='black')
canv.grid(row=0, column=2)

Label(root, width=30, text="FMbK", font=("Helvetica", 14), fg="black").grid(row=5, column=2)
Button(root, width=30, text="Open a File", command=open_file).grid(row=45, column=2)
Button(root, width=30, text="Copy a File", command=copy_file).grid(row=25, column=2)
Button(root, width=30, text="Delete a File", command=delete_file).grid(row=35, column=2)
Button(root, width=30, text="Rename a File", command=rename_file).grid(row=45, column=2)
Button(root, width=30, text="Move a File", command=move_file).grid(row=55, column=2)
Button(root, width=30, text="Make a Folder", command=make_folder).grid(row=75, column=2)
Button(root, width=30, text="Remove a Folder", command=remove_folder).grid(row=65, column=2)
Button(root, width=30, text="List all Files in Directory", command=list_files).grid(row=85, column=2)
root.mainloop()
