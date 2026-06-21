from tkinter import Tk, Button, Label
from tkinter import ttk
import threading
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

    # disable UI while processing
    start_button.config(state="disabled")
    select_button.config(state="disabled")

    progress.config(maximum=100)
    progress.config(value=0)

    def worker():
        import shutil

        from extract_faces import extract_faces
        from generate_embeddings import generate_embeddings
        from cluster_faces import cluster_faces
        from organize_faces import organize_faces

        def ui_set_label(text):
            window.after(0, lambda: folder_label.config(text=text))

        def ui_set_progress(val):
            window.after(0, lambda: progress.config(value=val))

        def ui_enable():
            window.after(0, lambda: start_button.config(state="normal"))
            window.after(0, lambda: select_button.config(state="normal"))

        ui_set_label("Extracting faces...")
        ui_set_progress(5)

        if os.path.exists("faces"):
            try:
                shutil.rmtree("faces")
            except Exception:
                pass

        if os.path.exists("clustered_faces"):
            try:
                shutil.rmtree("clustered_faces")
            except Exception:
                pass

        os.makedirs("faces", exist_ok=True)

        extract_faces(selected_folder)
        ui_set_progress(35)

        ui_set_label("Generating embeddings...")
        embeddings, valid_files = generate_embeddings()

        if len(embeddings) == 0:
            ui_set_label("No valid faces found!")
            ui_set_progress(0)
            ui_enable()
            return

        ui_set_progress(65)

        ui_set_label("Clustering faces...")
        labels = cluster_faces(embeddings, valid_files)

        ui_set_progress(85)

        organize_faces(valid_files, labels)

        ui_set_progress(100)
        ui_set_label("Finished!\nResults saved in clustered_faces")
        ui_enable()

    thread = threading.Thread(target=worker, daemon=True)
    thread.start()


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