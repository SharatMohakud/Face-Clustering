from deepface import DeepFace

result = DeepFace.represent(
    img_path="faces/face_0.jpg",
    model_name="Facenet"
)

print(type(result))
print(result[0].keys())

embedding = result[0]["embedding"]

print("Embedding length:", len(embedding))
print("First 10 values:")
print(embedding[:10])