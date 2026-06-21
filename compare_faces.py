from deepface import DeepFace

result = DeepFace.verify(
    img1_path="faces/face_0.jpg",
    img2_path="faces/face_1.jpg",
    model_name="Facenet"
)

print("Same person:", result["verified"])
print("Distance:", result["distance"])
print("Threshold:", result["threshold"])