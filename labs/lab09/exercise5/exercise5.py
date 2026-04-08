import pandas as pd


def high_performers(filename):
    
    df = pd.read_csv(filename)
    
    
    
    score_column = df[["Math","Science","English","Physics","Chemistry"]]

    high_score = df(df[score_column] > 85)

    names = set(high_score["names"])
    

    return { 
        "count" : len(names),
        "names" : names
        }


result = high_performers("CP125-Class-Repo/labs/lab09/data/students.csv")
print(result)
# {
#     "count": 8,
#     "names": {"Ali", "Sara", "Hassan", "Fatima", "Omar", "Layla", "Yusuf", "Amira"}
# }