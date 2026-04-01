import pandas as pd
import matplotlib.pyplot as plt


def show_math_trend(filename):
    
    df = pd.read_csv(filename)

    math_score = df["Math"]

    

    plt.plot(df.index, math_score)              # Create line (x=horizontal, y=vertical)
    plt.xlabel("Student Index") # Label x-axis
    plt.ylabel("Math Score")     # Label y-axis
    plt.title("Math Scores Trends")     # Add title
    plt.show()                   # Display (required!)

    return len(df)



count = show_math_trend("CP125-Class-Repo/labs/lab09/data/students.csv")
# Chart window appears showing Math scores
