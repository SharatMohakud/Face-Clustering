import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory

from extract_faces import extract_faces
from generate_embeddings import generate_embeddings
from cluster_faces import cluster_faces
from organize_faces import organize_faces


root = Tk()
root.withdraw()

selected_folder = askdirectory(
    title="Select Photo Folder"
)

if not selected_folder:
    print("No folder selected")
    exit()

if os.path.exists("faces"):
    shutil.rmtree("faces")

if os.path.exists("clustered_faces"):
    shutil.rmtree("clustered_faces")

os.makedirs("faces")

print("Selected Folder:", selected_folder)

# Step 1
extract_faces(selected_folder)

# Step 2
embeddings, valid_files = generate_embeddings()

# Step 3
labels = cluster_faces(
    embeddings,
    valid_files
)

# Step 4
organize_faces(
    valid_files,
    labels
)

print("\nAll Done!")


















