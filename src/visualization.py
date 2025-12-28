import matplotlib.pyplot as plt
import seaborn as sns


def plot_amount_distribution(df, save_path=None):
    plt.figure(figsize=(8,5))
    sns.histplot(df['Amount'], bins=50, kde=True)
    plt.title("Transaction Amount Distribution")
    if save_path:
        plt.savefig(save_path)
    plt.show()


def plot_anomaly_scores(scores, save_path=None):
    plt.figure(figsize=(8,5))
    sns.histplot(scores, bins=50)
    plt.title("Anomaly Score Distribution")
    if save_path:
        plt.savefig(save_path)
    plt.show()
