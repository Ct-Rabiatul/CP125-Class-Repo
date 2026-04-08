import pandas as pd
import matplotlib.pyplot as plt


def plot_subject_maximums(filename):

    df = pd.read_csv(filename)

    subjects = ["Math", "Science", "English", "Physics", "Chemistry"]

    max_scores = df[subjects].max()

    plt.plot(subjects, max_scores, marker='o')              # Create line (x=horizontal, y=vertical)
    plt.xlabel("Subject") # Label x-axis
    plt.ylabel("Maximum Score")     # Label y-axis
    plt.title("Maximum Scores by Subject")     # Add title
    plt.show()                   # Display (required!)

    return len(df)