import pandas as pd


def compare_averages(filename):
    
    df = pd.read_csv(filename)

    math_avg = df["Math"].mean()
    science_avg = df["Science"].mean()
    eng_avg = df["English"].mean()

    subj = []
    for i in subj:
        subj.append(i)
    
    best_subj = max(subj)

    worst_subj = min(subj)

    return {
        "Math" : math_avg ,
        "Science" : science_avg ,
        "English" : eng_avg ,
        "best_subject" : best_subj ,
        "worst_subject" : worst_subj
    }
    


