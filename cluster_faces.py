from sklearn.cluster import DBSCAN


def cluster_faces(embeddings, files_used):

    clustering = DBSCAN(
        eps=0.5,
        min_samples=1,
        metric="cosine"
    )

    labels = clustering.fit_predict(embeddings)

    print("\nClusters:\n")

    for file, label in zip(files_used, labels):
        print(f"{file} --> Person {label}")

    return labels


if __name__ == "__main__":
    print("Run from main.py")