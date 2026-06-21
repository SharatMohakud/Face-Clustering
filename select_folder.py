from tkinter import Tk
from tkinter.filedialog import askdirectory

root = Tk()
root.withdraw()

folder = askdirectory(
    title="Select Photo Folder"
)

print(folder)