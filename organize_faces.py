import os
import shutil


def organize_faces(files_used, labels):

    output_folder = "clustered_faces"

    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)

    os.makedirs(output_folder)

    for file, label in zip(files_used, labels):

        person_folder = os.path.join(
            output_folder,
            f"Person_{label}"
        )

        os.makedirs(person_folder, exist_ok=True)

        src = os.path.join("faces", file)
        dst = os.path.join(person_folder, file)

        shutil.copy(src, dst)

    print("Finished!")


if __name__ == "__main__":
    print("Run from main.py")