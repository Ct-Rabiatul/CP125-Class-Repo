#SITI RABIATUL ADAWIAH

import csv

def find_average_height (bmi_file):

    f = open(bmi_file, "r", newline="")
    bmi = csv.reader(f)

    total = 0
    count = 0
    next(bmi)
    for row in bmi:

        height = float(row[1])
        total += height
        count += 1
    
    average = total / count

    f.close()

    return average

result = find_average_height("CP125-Class-Repo/labs/lab-test-3/data/bmi.csv")
print(result)

def insert_own_data (bmi_file, data):

    f = open(bmi_file, "w+", newline="")
    bmi = csv.writer(f)

    bmi.writerow(data)
    
    f.close()
    print(bmi)

data = ["Female", 150, 36, 13]
result = insert_own_data("CP125-Class-Repo/labs/lab-test-3/data/bmi1.txt", data)
print(result)






