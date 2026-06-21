from deepface import DeepFace
import os


def generate_embeddings():

    embeddings = []
    valid_files = []

    files = os.listdir("faces")

    for file in files:

        path = os.path.join("faces", file)

        try:
            result = DeepFace.represent(
                img_path=path,
                detector_backend= "retinaface",
                model_name="ArcFace"
            )

            embedding = result[0]["embedding"]

            embeddings.append(embedding)
            valid_files.append(file)

            print(f"Processed: {file}")

        except Exception:
            print(f"Skipped: {file}")

    print()
    print("Total valid embeddings:", len(embeddings))

    return embeddings, valid_files


if __name__ == "__main__":
    generate_embeddings()