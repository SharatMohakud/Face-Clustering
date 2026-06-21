import os
import shutil

print("Cleaning folders...")

for folder in ["faces", "clustered_faces"]:

    if os.path.exists(folder):
        shutil.rmtree(folder)

    os.makedirs(folder)

print("Folders cleaned!")

print("Extracting faces...")

exec(open("extract_faces.py").read())

print("Face extraction completed!")

print("Clustering faces...")

exec(open("organize_faces.py").read())

print("Clustering completed!")