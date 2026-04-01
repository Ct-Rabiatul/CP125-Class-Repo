import pandas as pd
import matplotlib.pyplot as plt


def show_science_distribution(filename):

    df = pd.read_csv(filename)

    science_score = df["Science"]
    
    plt.hist(science_score, bins=10)  # bins=10 is standard
    plt.xlabel("Science Score")
    plt.ylabel("Frequency")
    plt.title("Science Score Distribution")
    plt.show()

count = show_science_distribution("CP125-Class-Repo/labs/lab09/data/students.csv")
# Chart window appears showing Math scores