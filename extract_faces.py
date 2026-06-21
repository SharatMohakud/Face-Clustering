import cv2
import os


def extract_faces(folder_path):

    files = os.listdir(folder_path)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    count = 0

    for file in files:

        path = os.path.join(folder_path, file)

        image = cv2.imread(path)

        if image is None:
            continue

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=6,
            minSize=(80, 80)
        )

        for (x, y, w, h) in faces:

            face = image[y:y+h, x:x+w]

            save_path = f"faces/face_{count}.jpg"

            cv2.imwrite(save_path, face)

            count += 1

    print("Finished")


if __name__ == "__main__":
   extract_faces("dataset")