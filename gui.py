from tkinter import Tk, Button, Label
from tkinter import ttk
from tkinter.filedialog import askdirectory
import os

selected_folder = ""


def select_folder():

    global selected_folder

    folder = askdirectory(
        title="Select Photo Folder"
    )

    if folder:

        selected_folder = folder

        folder_label.config(
            text=f"Selected:\n{folder}"
        )


def start_clustering():

    if not selected_folder:

        folder_label.config(
            text="Please select a folder first!"
        )

        return

    import shutil

    from extract_faces import extract_faces
    from generate_embeddings import generate_embeddings
    from cluster_faces import cluster_faces
    from organize_faces import organize_faces

    folder_label.config(
        text="Extracting faces..."
    )

    window.update()

    if os.path.exists("faces"):
        shutil.rmtree("faces")

    if os.path.exists("clustered_faces"):
        shutil.rmtree("clustered_faces")

    os.makedirs("faces")

    extract_faces(selected_folder)

    folder_label.config(
        text="Generating embeddings..."
    )

    window.update()

    embeddings, valid_files = generate_embeddings()

    if len(embeddings) == 0:

        folder_label.config(
            text="No valid faces found!"
        )

        return

    folder_label.config(
        text="Clustering faces..."
    )

    window.update()

    labels = cluster_faces(
        embeddings,
        valid_files
    )

    organize_faces(
        valid_files,
        labels
    )

    folder_label.config(
        text="Finished!\nResults saved in clustered_faces"
    )


def open_results():

    if os.path.exists("clustered_faces"):
        os.startfile("clustered_faces")
    else:
        folder_label.config(
            text="No results found yet!"
        )


window = Tk()

window.title("Face Clustering System")
window.geometry("600x400")

title = Label(
    window,
    text="Face Clustering System",
    font=("Arial", 18)
)

title.pack(pady=20)

select_button = Button(
    window,
    text="Select Folder",
    width=20,
    height=2,
    command=select_folder
)

select_button.pack(pady=10)

start_button = Button(
    window,
    text="Start Clustering",
    width=20,
    height=2,
    command=start_clustering
)

start_button.pack(pady=10)

open_button = Button(
    window,
    text="Open Results",
    width=20,
    height=2,
    command=open_results
)

open_button.pack(pady=10)

folder_label = Label(
    window,
    text="No folder selected",
    wraplength=550
)
progress = ttk.Progressbar(
    window,
    length=400,
    mode="determinate"
)

progress.pack(pady=10)
folder_label.pack(pady=20)

window.mainloop()