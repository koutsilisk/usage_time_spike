# https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_plusplus.html#sphx-glr-auto-examples-cluster-plot-kmeans-plusplus-py
from sklearn.cluster import kmeans_plusplus
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from time import process_time_ns


def run():

    t1_start = process_time_ns()

    # Generate sample data
    n_samples = 4000
    n_components = 4

    X, y_true = make_blobs(
        n_samples=n_samples, centers=n_components, cluster_std=0.60, random_state=0
    )
    X = X[:, ::-1]

    # Calculate seeds from kmeans++
    centers_init, indices = kmeans_plusplus(X, n_clusters=4, random_state=0)

    # Plot init seeds along side sample data
    plt.figure(1)
    colors = ["#4EACC5", "#FF9C34", "#4E9A06", "m"]

    for k, col in enumerate(colors):
        cluster_data = y_true == k
        plt.scatter(X[cluster_data, 0], X[cluster_data, 1], c=col, marker=".", s=10)

    plt.scatter(centers_init[:, 0], centers_init[:, 1], c="b", s=50)
    plt.title("K-Means++ Initialization")
    plt.xticks([])
    plt.yticks([])

    t1_stop = process_time_ns()

    print(f"Elapsed time during the whole program in nanoseconds:{t1_stop - t1_start}")
    return


if __name__ == "__main__":
    run()
    plt.show()
